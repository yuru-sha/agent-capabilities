# Media

SmartNews exposes ad-account media management for images and videos.

## Listing

Media listing is paginated and supports filters such as media type, dimensions,
aspect ratio, search query, sort, `page_size`, and `page`.

## Upload

Media creation uses `multipart/form-data` with:

- `file_name`
- `media_type` (`IMAGE` or `VIDEO`)
- binary `media_file`

The API may return an existing media-file resource when the same file was
previously uploaded under the same ad account.

## Implementation guidance

- Stream file bodies from disk/object storage.
- Avoid reading an entire video into memory.
- Set explicit request/body timeouts appropriate for upload size.
- Preserve cancellation.
- After upload, inspect processing/availability fields before creating dependent ads.
- Never blindly retry an upload after an ambiguous transport failure without checking whether the media already exists.
