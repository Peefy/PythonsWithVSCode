# python app.py 
import numpy as nm
from socket import socket, AF_INET, SOCK_DGRAM

class Udpsocket():
    '''
    Udpsocket类，建立udp socket服务端
    用法：
        p = Udpsocket.Udpsocket()
        p.listen()
        无限循环监听端口，process重写数据处理方式
    '''
        
    def __init__( self ):
        '''
        初始化，建立socket，ip端口绑定
        '''
        self.udpServerSocket = socket( AF_INET, SOCK_DGRAM )
        self.udpServerSocket.bind( ('101.5.242.62', 16384) )
        self.buffer_size = 1024 #缓冲区为1k
            
            
    def receive( self ):
        '''
        收取端口传来的数据
        '''
        raw_data, addr = self.udpServerSocket.recvfrom( int(self.buffer_size) )
        print('conn from :', addr )
        typeNum = int(raw_data[0:2])
        print('receive from udp client : ', str(raw_data))
        print(typeNum)

        return ( raw_data, addr )
            

    def process( self, data ):
        '''
        socket传输的数据加工处理，继承重写该函数
        '''
        result = data
        return result

        
    def send( self, addr, result ):
        '''
        返回信息
        '''
        self.udpServerSocket.sendto( result, addr )
            
        
    def listen( self ):
        '''
        监听端口，无限循环
        '''
        while True:
            print ('wait for connect')
            #self.udpServerSocket.send('asdad')
            ( raw_data, addr ) = self.receive()             #接收数据
            print(addr)
            self.send(addr, 'ss')
            #result = self.process( socket_data[0] )  #处理接收的信息
            #self.send( socket_data[1], str(result) ) #返回数据
            #self.close()
        
        
    def close( self ):
        '''
        关闭连接
        '''
        self.udpServerSocket.close()

            
        def __del__( self ):
            self.close()

X = [1, 3, 6, 2, 4]
X = nm.sort(X)
print(X)            
p = Udpsocket()
p.listen()
