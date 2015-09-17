package main

import (    
    "encoding/base32"
    "fmt"
    "strings"
     )

var bytes [10]byte
  /*//This is a start for a better way to do this, 
    //maybe generate them one at a time and we can just crawl from go too...

func next_number () []byte{
    for i :=
    bytes[9]
    return bytes[:]
}
*/
func main() {

//LETS DO IT THE DUMB WAAAY

//10 loops for 10 bytes
for { 
for {
for {
for {
for {
for {
for {
for {
for {
for {
    bytes[9] += 1
    str := base32.StdEncoding.EncodeToString( bytes[:] )
    fmt.Println(strings.ToLower(str) )
    if bytes[9] == 255 {
        bytes[9] = 0
        break
    }
    }

    bytes[8] += 1
    str := base32.StdEncoding.EncodeToString( bytes[:] )
    fmt.Println(strings.ToLower(str) )
    if bytes[8] == 255 {
        bytes[8] = 0
        break
    }
    }

    bytes[7] += 1
    if bytes[7] == 255 {
        bytes[7] = 0
        break
    }
    }

    bytes[6] += 1
    if bytes[6] == 255 {
        bytes[6] = 0
        break
    }
    }

    bytes[5] += 1
    if bytes[5] == 255 {
        bytes[5] = 0
        break
    }
    }

    bytes[4] += 1
    if bytes[4] == 255 {
        bytes[4] = 0
        break
    }
    }

    bytes[3] += 1
    if bytes[3] == 255 {
        bytes[3] = 0
        break
    }
    }

    bytes[2] += 1
    if bytes[2] == 255 {
        bytes[2] = 0
        break
    }
    }

    bytes[1] += 1
    if bytes[1] == 255 {
        bytes[1] = 0
        break
    }
    }

    bytes[0] += 1
    if bytes[0] == 255 {
        bytes[0] = 0
        break
    }
    }


}