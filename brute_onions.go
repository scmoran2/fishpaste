package main

import (    
    "encoding/base32"
    "fmt"
    "strings"
     )

func main() {

var bytes [10]byte

for i:=0; i  < 10; i++ {

for j:=0; j  < 10; j++ {

for k:=0; k  < 10; k++ {

for l:=0; l  < 10; l++ {

for m:=0; m  < 10; m++ {

for n:=0; n  < 10; n++ {

for o:=0; o  < 10; o++ {

for p:=0; p  < 10; p++ {

for q:=0; q < 10; q++ {

bytes[q] += 1
str := base32.StdEncoding.EncodeToString( bytes[:] )
fmt.Println(strings.ToLower(str) )
if bytes[q] == 255 {
    bytes[q] = 0
    break
}
}

bytes[p] += 1
if bytes[p] == 255 {
    bytes[p] = 0
    break
}
}

bytes[o] += 1
if bytes[o] == 255 {
    bytes[o] = 0
    break
}
}

bytes[n] += 1
if bytes[n] == 255 {
    bytes[n] = 0
    break
}
}

bytes[m] += 1
if bytes[m] == 255 {
    bytes[m] = 0
    break
}
}

bytes[l] += 1
if bytes[l] == 255 {
    bytes[l] = 0
    break
}
}

bytes[k] += 1
if bytes[k] == 255 {
    bytes[k] = 0
    break
}
}

bytes[j] += 1
if bytes[j] == 255 {
    bytes[j] = 0
    break
}
}

bytes[i] += 1
if bytes[i] == 255 {
    bytes[i] = 0
    break
}
}


}
