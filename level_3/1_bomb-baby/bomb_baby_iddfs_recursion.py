def solution(M, F):
    def limited_dfs(root_node, target_node, depth_limit):
        if root_node == target_node:
            return True

        if depth_limit <= 0:
            return False

        mach = root_node[0]
        facula = root_node[1]

        left_child = (mach + facula, facula)
        right_child = (mach, facula + mach)
        if limited_dfs(left_child, target_node, depth_limit - 1) or limited_dfs(right_child, target_node,
                                                                                depth_limit - 1):
            return True

        return False

    tm = long(M)
    tf = long(F)

    max_depth = max(tm, tf)
    root = (long(1), long(1))
    for current_depth_limit in range(max_depth):
        if limited_dfs(root, (tm, tf), current_depth_limit):
            return str(current_depth_limit)
    return "impossible"
