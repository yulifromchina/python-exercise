# 死锁的4个必要条件：
# 1.互斥条件：所分配的资源都是排他性使用
# 2.请求和保持条件：进程至少保持类一个资源，又请求新的资源
# 3.不剥夺条件
# 4.循环等待条件


# 死锁问题很大一部分是由于线程同时获取多个锁造成的，避免死锁的方案1：每个线程只允许一个锁，破坏条件2
# 方案2：为程序中的每个锁分配一个id，只允许按照升序规则来获取锁，破坏条件4
# 方案3：使用看门狗定时器，看门狗计算器不断自增，每隔一段时间清零一次，如果出现类死锁，造成看门狗计算器无法清零，
# 溢出发生定时器超时，这时程序通过重新启动恢复正常状态

