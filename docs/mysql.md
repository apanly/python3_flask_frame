### 数据库变更历史

```
CREATE DATABASE `python3_flask_frame` DEFAULT COLLATE = `utf8mb4_general_ci`;

CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL DEFAULT '' COMMENT '用户名',
  `email` varchar(50) NOT NULL DEFAULT '' COMMENT '邮箱地址也是登录用户名',
  `salt` varchar(64) NOT NULL DEFAULT '' COMMENT '随机码',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE = `utf8mb4_general_ci`  COMMENT='用户表';

INSERT INTO `user` (`id`, `name`, `email`, `salt`)
VALUES
	(1, '郭威', '你的邮箱', 'xxxxx');

```