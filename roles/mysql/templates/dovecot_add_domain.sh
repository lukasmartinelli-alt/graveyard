#!/bin/bash
virtual_domain=$1
domain_id=$2
mysql -u {{ mysql_user }} -p{{ mysql_pass }} << EOF
INSERT IGNORE INTO mailserver.virtual_domains
  (id ,name)
  VALUES
  ('$domain_id', '$virtual_domain');
EOF

echo "Created domain $virtual_domain"
echo "Use the id $domain_id to add new users"
