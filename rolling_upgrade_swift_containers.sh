for name in $(docker ps | awk '{if(NR>1) print $NF}' | grep swift)
do
	new_name=$name'_ocata'
	docker stop $name
    docker start $new_name
done