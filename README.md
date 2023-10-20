# Test case for AppIndicator bug in Mate-Fedora
To run this test case type:
```
python3 testcase.py
```

Every 5 seconds normal icon should change to attention icon (and vice versa) and attention label count should increase by 1.

## Results
### GNOME attention icon (works as expected)
![image](results/attention-GNOME.png)

### Mate attention icon (shows normal icon instead of attention icon)
![image](results/attention-Mate.png)

### Mate normal icon (works as expected)
![image](results/normal-Mate.png)
