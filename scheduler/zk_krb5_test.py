import os
import socket
import time

from kazoo.client import KazooClient
from kazoo.recipe.election import Election

if socket.gethostname().startswith("linux"):
    KRB5_CONFIG = "/etc/krb5.conf"
    CLIENT_JVMFLAGS = '/opt/zookeeper-kerberos/conf/client-jaas.conf'
else:
    KRB5_CONFIG = '/Users/wind/projects/pyspark-learn/scheduler/data/krb5.conf'
    CLIENT_JVMFLAGS = '-Djava.security.auth.login.config=/Users/wind/projects/pyspark-learn/scheduler/data' \
                      '/client-jaas.conf'


def hell():
    print("hello")


def start():
    # 指定远程 krb5.conf 文件的路径
    os.environ['KRB5_CONFIG'] = KRB5_CONFIG
    os.environ['CLIENT_JVMFLAGS'] = CLIENT_JVMFLAGS
    # ZooKeeper集群的Kerberos认证信息
    zk_hosts = 'linux01:2182,linux02:2182,linux03:2182'
    # zk_hosts = 'linux01:2181,linux02:2181,linux03:2181'

    client = KazooClient(hosts=zk_hosts)

    # 连接到ZooKeeper服务器
    client.start()

    # 在这里执行您的操作
    # 定义一个路径，用于在 ZooKeeper 中创建一个 znode 用于选举
    election_path = "/example/election"

    # 创建一个选举对象
    election = Election(client, election_path)

    # 参与选举
    # 使用分布式锁
    # lock_path = "/example/lock"
    # lock = Lock(client, lock_path)
    #
    # with lock:  # 这里会尝试获取锁，只有成功获取锁的节点能够继续执行选举
    #     election.run(hello)

    election.run(hell)

    time.sleep(10)

    # 关闭连接
    client.stop()
    client.close()


if __name__ == '__main__':
    start()

