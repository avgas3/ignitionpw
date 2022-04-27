# ignitionpw
Ansible Filter Plugin for encrypting/decrypting passwords in config.idb

Ignition uses a not-so-hidden encryption to store passwords that must be exposed to other services in its internal database. This allows us to perform this encryption and decryption as an Ansible fitler. 

## prereq
`pip install pyDes`

## installation

`cp ignitionpw.py {ansible install directory}/plugins/filter`

## usage
`ansible-playbook testplaybook.yml`
