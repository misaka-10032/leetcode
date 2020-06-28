# Shortest Distance from All Buildings

* Each 0 marks an empty land which you can pass by freely.
* Each 1 marks a building which you cannot pass through.
* Each 2 marks an obstacle which you cannot pass through.

```
1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
```

* Build ONE building on land, such that we have smallest
  distance to all the other buildings.
* Return the smallest building; -1 if impossible.