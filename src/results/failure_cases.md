# Failure Cases

I manually inspected failed episodes on the val_unseen split. Here are the most common failure modes.

## 1. Looping Behavior

The agent repeatedly turns left or right without moving forward. This happened in about 30% of failed episodes. The Action History Encoder was added to reduce this, but it only helped slightly.

## 2. Wrong Room

The agent navigates to a different room and stops there. This usually happens when the instruction mentions a common object like "sofa" or "table" that appears in multiple rooms.

## 3. Premature Stopping

The agent stops before reaching the target. In some cases, it stops in the middle of a hallway.

## 4. Collision

The agent gets stuck against walls or furniture. The policy does not have a collision penalty, so it sometimes keeps moving forward into obstacles.

## 5. Instruction Neglect

The agent ignores the language instruction and follows a generic path, such as always turning right at intersections.

## Example Trajectory

- Episode ID: 1420
- Instruction: "Go past the kitchen and stop near the sofa."
- Result: The agent turned left three times, then moved forward into a bedroom and stopped.
- Distance to target: 9.2 m
- Success: No
