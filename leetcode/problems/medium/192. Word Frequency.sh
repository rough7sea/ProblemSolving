awk '
{
    for (i = 1; i <= NF; i++)  {
        count = 0
        for (key in my_dict) {
            if (key == $i) {
              count = my_dict[key]
              break
            }
        }
        my_dict[$i] = count + 1
    }
}
END {
#    qsort(my_dict)
    for (key in my_dict) {
        print key, my_dict[key] | "sort -k2 -n -r"
    }
}' words.txt



#declare -A dict
#while read line; do
#    for word in $line; do
#        if [ ${dict[$word]} ]; then
#            (( dict[$word]++ ))
#        else
#            dict[$word]=1
#        fi
#    done
#done < words.txt
#
#for word in "${!dict[@]}"; do
#    echo $word ${dict[$word]}
#done | sort -rn -k2