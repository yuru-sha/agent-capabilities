---
name: reply-to-review-thread
description: Reply to an existing GitHub pull request review thread, including an inline comment, after explicit user authorization. Use when the user asks to answer in the original review thread; do not use for top-level PR comments, new review comments, review requests, or resolution alone.
---

# Reply to a pull request review thread

Use this skill only for an explicitly requested reply to an existing review
thread. This is an external mutation: resolve one exact PR and one exact
thread, send the approved body, and verify the stored reply.

1. Resolve the exact PR and current head with
   `gh pr view <pr> --json number,url,state,headRefOid`. Stop if it is missing,
   closed, or belongs to another repository.
2. Query the PR's GraphQL `reviewThreads` connection and its `comments`
   connection. Match the requested path, line, author, and comment body, then
   record the thread node ID, parent comment node ID, and initial
   `isResolved` value. Require one unique match and `viewerCanReply: true`.
3. Keep the ID types separate. `PullRequestReviewThread.id` is the thread ID
   (normally `PRRT_...`); numeric REST review-comment IDs and GraphQL comment
   IDs such as `PRRC_...` identify comments, not threads. If only a comment ID
   is available, resolve the thread through `reviewThreads` before mutating.
4. Reply with GraphQL `addPullRequestReviewThreadReply`, passing the `PRRT_...`
   value as `pullRequestReviewThreadId` and the approved text as a `body`
   variable:

   ```graphql
   mutation Reply($threadId: ID!, $body: String!) {
     addPullRequestReviewThreadReply(input: {
       pullRequestReviewThreadId: $threadId
       body: $body
     }) {
       comment { id databaseId body replyTo { id } }
     }
   }
   ```

   Pass multiline text as a real value from a body file or equivalent GraphQL
   variable. Preserve line feeds; do not submit a literal `\\n` string.
5. Use the returned comment ID to re-fetch the same thread and verify the
   exact body, the expected `replyTo` parent, and the same thread/path. A REST
   `in_reply_to`, `inReplyTo`, top-level `gh pr comment`, or deprecated
   `addPullRequestReviewComment` path is not a fallback for this operation. If
   the GraphQL thread mutation is unavailable, stop without posting elsewhere.
6. Re-fetch and compare `isResolved` with the recorded value. Leave resolution
   unchanged unless the user explicitly requested it; only then call
   `resolveReviewThread` with the same thread ID and verify `isResolved: true`.

Do not claim success from the mutation response alone. The stored comment,
parent linkage, thread identity, and requested resolution state are the
completion criteria.
