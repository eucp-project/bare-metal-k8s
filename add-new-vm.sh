#! /bin/bash

node=$1
echo $node
#vmid=$(python3 startvm-hpc.py 11483 --name $node | cut -d' ' -f6)
vmid=$node

while true;
do
		state=$(python3 getvm.py $vmid | cut -d' ' -f6,7)
		if [ "$state" == "('ACTIVE', 'RUNNING')" ]
		then
				ip=$(python3 getvm.py 68247 | cut -d' ' -f4)
				break
		fi
		sleep 2
done
echo $ip
nodename=$(python3 add-node-to-hosts.py $ip)

# give the new machine some time to update itself
sleep 15

export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i hosts.ini --become --user ubuntu playbook.yml -vv

#python3 update-storage.py $nodename
