for name in {1..500};

do

    swift upload --object-name 'delete_objects'.$name daidv test_object

done
