#!/usr/bin/python
import sys
import os
from mininet.topo import Topo, LinearTopo
from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController, Switch


class single(Topo):
    def __init__(self, k=1):
        Topo.__init__(self)
        "Create host and switch"
        "k: number host connect in switch"
        "Init k"
        self.k = k
        "Init 1 switch"
        s1 = self.addSwitch('s1')
        for h in range(k):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(s1, host)


def addController():
    "ip_controller_default='10.0.0.128'"
    "Input ip address of controller"
    ip_controller = str(raw_input('What address ip of controller ? \n '))
    c0 = RemoteController('c0', ip=ip_controller, port=6653)
    return c0


def choose_type():
    print('Do you use topology network for mininet ? \n')
    type_topo = int(raw_input(
        'Press number for choose type network have: 1(tree network) | 2(linear network) | 3(single network) '))
    if type_topo == 1:
        print('You have to choose tree network ')
    elif type_topo == 2:
        print('You have to choose linear network ')
    elif type_topo == 3:
        print('You have to choose single network ')

    return type_topo


def tree_network():
    "Input number deepth for tree network "
    depth1 = int(raw_input('How many depth in tree network? \n '))
    "Input number fanout for tree network "
    fanout1 = int(raw_input('How many fanout in tree network? \n '))
    tree = TreeTopo(depth=depth1, fanout=fanout1)
    net = Mininet(topo=tree, build=False)
    net.addController(addController())
    net.build()
    net.addNAT().configDefault()
    net.start()
    CLI(net)


def linear_network():
    "Input number of switches"
    k1 = int(raw_input('How many switch in linear network ? \n'))
    "Input of number hosts per switch"
    n1 = int(raw_input('How many host per switch ? \n'))
    linear = LinearTopo(k=k1, n=n1)
    net = Mininet(topo=linear, build=False)
    net.addController(addController())
    net.build()
    net.addNAT().configDefault()
    net.start()
    CLI(net)


def single_network():
    k2 = int(raw_input('How many host connect in switch ? \n'))
    node = single(k2)
    net = Mininet(topo=node, build=False)
    net.addController(addController())
    net.build()
    net.addNAT().configDefault()
    net.start()
    CLI(net)


def clear():
    os.system('sudo mn -c')


def main():
    clear()
    type = choose_type()
    if type == 1:
        tree_network()
    elif type == 2:
        linear_network()
    elif type == 3:
        single_network()


main()