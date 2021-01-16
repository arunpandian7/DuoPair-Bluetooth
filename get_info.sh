#!/bin/bash

sudo cat /var/lib/bluetooth/$1/$2/info > $2.config 2>/dev/null