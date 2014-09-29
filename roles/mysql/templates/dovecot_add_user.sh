#!/bin/bash
user=$1
password=$2
user_domain_id=$3
user_id=$4
hashed_password=`doveadm pw -s SHA512-CRYPT << EOF
$password
$password
EOF`
sanitized_password=$hashed_password | sed 's/^{SHA512-CRYPT}//' | tr -d '\n'
mysql -u {{ mysql_user }} -p{{ mysql_pass }} << EOF
INSERT IGNORE INTO mailserver.virtual_users
(id, domain_id, password , email)
VALUES
('$user_id', '$user_domain_id', '$sanitized_password', '$user');
EOF
echo "User $user with password $password created"
