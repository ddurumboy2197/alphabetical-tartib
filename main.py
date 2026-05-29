def list_alphabetical_sort(lst):
    return sorted(lst)

sozlar = ["apple", "banana", "cherry", "date", "elderberry"]
print(list_alphabetical_sort(sozlar))
```

```python
def list_alphabetical_sort(lst):
    return sorted(lst, key=str.lower)

sozlar = ["Apple", "banana", "Cherry", "date", "elderberry"]
print(list_alphabetical_sort(sozlar))
