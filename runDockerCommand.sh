#!/bin/bash
echo "$2" | sudo -S docker run "$1"
