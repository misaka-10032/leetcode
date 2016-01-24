# Longest Substring Without Repeating Characters

## Description
* [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* Input: s, type: str
* Return: longest, type: int

## Solution

* Maintain front and rear index, within which is the current non-repeating substring.
* Maintain a set to record appeared chars.
* Be careful of empty string.