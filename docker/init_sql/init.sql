SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;
USE zbn_db
-- ----------------------------
--  Table structure for `zbn_logs`
-- ----------------------------
DROP TABLE IF EXISTS `zbn_logs`;
CREATE TABLE `zbn_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(100) NOT NULL COMMENT '剧本ID',
  `app_uuid` varchar(100) NOT NULL COMMENT 'App UUID',
  `app_name` varchar(20) NOT NULL DEFAULT '' COMMENT 'APP 名字',
  `result` text NOT NULL COMMENT '执行结果',
  `create_time` datetime COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `zbn_type`
-- ----------------------------
DROP TABLE IF EXISTS `zbn_type`;
CREATE TABLE `zbn_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(2) NOT NULL DEFAULT '1' COMMENT '分类  1 剧本分类 2变量分类',
  `name` varchar(20) NOT NULL DEFAULT '' COMMENT '分类名称',
  `update_time` datetime COMMENT '更新时间',
  `create_time` datetime COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `zbn_type`
-- ----------------------------
BEGIN;
INSERT INTO `zbn_type` VALUES ('1', '1', '默认剧本', '2020-11-06 13:14:25', '2020-11-06 13:14:27');
COMMIT;

-- ----------------------------
--  Table structure for `zbn_user`
-- ----------------------------
DROP TABLE IF EXISTS `zbn_user`;
CREATE TABLE `zbn_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(20) NOT NULL DEFAULT '' COMMENT '账号',
  `passwd` varchar(32) NOT NULL DEFAULT '' COMMENT '密码',
  `nick_name` varchar(20) NOT NULL DEFAULT '' COMMENT '用户昵称',
  `email` varchar(50) NOT NULL DEFAULT '' COMMENT '用户邮箱',
  `token` varchar(32) NOT NULL DEFAULT '' COMMENT 'Token 用户唯一标识',
  `update_time` datetime COMMENT '更新时间',
  `create_time` datetime COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_account` (`account`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `zbn_user`
-- ----------------------------
BEGIN;
INSERT INTO `zbn_user` VALUES ('1', 'admin', '3C830D97FC5AE3E9F9D1F491735C7AEA', '织布鸟', 'admin@zbn.io', '', '2020-11-06 10:51:30', '2020-10-22 17:58:32');
COMMIT;

-- ----------------------------
--  Table structure for `zbn_variablen`
-- ----------------------------
DROP TABLE IF EXISTS `zbn_variablen`;
CREATE TABLE `zbn_variablen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) NOT NULL DEFAULT '0' COMMENT '分类ID',
  `key` varchar(20) NOT NULL DEFAULT '' COMMENT '变量 KEY',
  `value` varchar(255) NOT NULL DEFAULT '' COMMENT '变量 值',
  `update_time` datetime COMMENT '更新时间',
  `create_time` datetime COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index.key` (`key`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `zbn_workflow`
-- ----------------------------
DROP TABLE IF EXISTS `zbn_workflow`;
CREATE TABLE `zbn_workflow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(100) NOT NULL DEFAULT '' COMMENT 'UUID',
  `user_id` int(11) NOT NULL DEFAULT '0' COMMENT '创建人',
  `type_id` int(11) NOT NULL DEFAULT '0' COMMENT '剧本分类',
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '剧本名称',
  `start_app` varchar(100) NOT NULL DEFAULT '' COMMENT '开始APP UUID',
  `end_app` varchar(100) NOT NULL DEFAULT '' COMMENT '结束APP UUID',
  `flow_json` text NOT NULL COMMENT '流程图画布数据',
  `flow_data` text NOT NULL COMMENT '流程图 APP 数据',
  `update_time` datetime COMMENT '更新时间',
  `create_time` datetime COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_uuid` (`uuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;
