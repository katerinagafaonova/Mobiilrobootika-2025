import sys
from tutorial_interfaces.srv import AddThreeInts
import rclpy
from rclpy.node import Node

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddThreeInts, 'add_three_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddThreeInts.Request()

    def send_request(self, a, b, c):
        self.req.a = int(a)
        self.req.b = int(b)
        self.req.c = int(c)
        self.future = self.cli.call_async(self.req)
        return self.future

def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 4:
        print('Usage: ros2 run py_srvcli client A B C')
        return 1

    node = MinimalClientAsync()
    future = node.send_request(sys.argv[1], sys.argv[2], sys.argv[3])

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            resp = future.result()
            node.get_logger().info(f'Result: {node.req.a} + {node.req.b} + {node.req.c} = {resp.sum}')
            break

    node.destroy_node()
    rclpy.shutdown()
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
