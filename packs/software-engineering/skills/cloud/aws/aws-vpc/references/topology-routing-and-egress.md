# Topology, routing, and egress

Plan VPC and subnet CIDRs for current workload density, multi-AZ growth, peering/TGW/hybrid overlap avoidance, and future service ENI demand.

A public subnet is defined by routing, not by workload intent. Internet-facing resources need an explicit public path; private workloads need explicit NAT, VPC endpoint, transit, or other egress design.

Keep route ownership clear across route tables, internet/NAT gateways, transit gateways, peering, VPN, and Direct Connect attachments.

Avoid single-AZ egress dependencies for multi-AZ workloads unless the failure and cross-AZ cost behavior is explicitly accepted.
