class Solution {
public:
    bool isRobotBounded(string instructions) {
        int dx = 0;
        int dy = 1;
        int x = 0;
        int y = 0;

        for (int i = 0; i < instructions.size() * 4; i++) {
            char instruction = instructions[i % instructions.size()];

            switch (instruction) {
                case 'G':
                    x += dx;
                    y += dy;
                    break;

                case 'L':
                    swap(dx, dy);
                    dx *= -1;
                    break;

                case 'R':
                    swap(dx, dy);
                    dy *= -1;
                    break;
            }
        }

        return x == 0 && y == 0;
    }
};