#!/usr/bin/env bash
# Download all mp3s from website
for i in `seq 1 50`; do
    while [[ ${#i} -lt 2 ]] ; do
        i="0${i}"
    done
    curl "http://prj.digimagic.com.tw/ntcmin700/mp3/page${i}.mp3" --output "page${i}.mp3" -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0' -H 'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5' -H 'Accept-Language: en-US,en;q=0.5' -H 'Referer: http://prj.digimagic.com.tw/ntcmin700/page24.htm' -H 'Range: bytes=0-' -H 'DNT: 1' -H 'Connection: keep-alive'
done
