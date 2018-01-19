# -*- coding:utf-8 -*-

import abc

class VmReceiver(object):
    """
    命令接收者，真正执行命令的地方
    """

    def start(self):
        print('Virtual machine start.')

    def stop(self):
        print('Virtual machine stop.')



class Command(object):
    """
    命令抽象类
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """
        命令对象只对外提供execute方法
        """
        pass


class StartVmCommand(Command):
    """
    开启虚拟机的命令
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.start()


class StopVmCommand(Command):
    """
    停止虚拟机的命令
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.stop()



class ClientInvoker(object):
    """
    命令调用者
    """

    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    receiver = VmReceiver()
    start_command = StartVmCommand(receiver)
    client = ClientInvoker(start_command)
    client.do()
    stop_command = StopVmCommand(receiver)
    client = ClientInvoker(stop_command)
    client.do()

