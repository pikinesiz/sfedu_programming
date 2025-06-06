import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RadarPublisher(Node):
    def __init__(self):
        super().__init__('radar_publisher')
        self.publisher_ = self.create_publisher(String, 'radar_data', 10)
        self.timer = self.create_timer(0.2, self.timer_callback)  # 5 Гц (было 1 Гц)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Radar Signal: {self.counter}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = RadarPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

4.3 Узел-подписчик (radar_subscriber.py)
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RadarSubscriber(Node):
    def __init__(self):
        super().__init__('radar_subscriber')
        self.subscription = self.create_subscription(
            String,
            'radar_data',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = RadarSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


Настройка точек входа (setup.py) 
entry_points={
    'console_scripts': [
        'radar_publisher = my_radar_pkg.radar_publisher:main',
        'radar_subscriber = my_radar_pkg.radar_subscriber:main',
    ],
},
