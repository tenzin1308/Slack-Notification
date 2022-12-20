#!/bin/sh -l

echo "hello $1"
time=$(date)
echo "succeed=$time" >> $GITHUB_OUTPUT