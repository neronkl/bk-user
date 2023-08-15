/**
 * 用户名
 * 由1-32位字母、数字、下划线(_)、点(.)、减号(-)字符组成，以字母或数字开头
 */
export const usernameRegx = {
  rule: /^[a-zA-Z0-9][0-9a-zA-Z]{0,31}$/,
  message: "由1-32位字母、数字、下划线(_)、点(.)、减号(-)字符组成，以字母或数字开头",
};

/**
 * 邮箱
 */
export const emailRegx = {
  rule: /^([A-Za-z0-9_\-.])+@([A-Za-z0-9_\-.])+\.[A-Za-z]+$/,
  message: "请输入正确的邮箱地址",
};

/**
 * 手机号
 */
export const telRegx = {
  rule: /^1[3-9]\d{9}$/,
  message: "请输入正确的手机号码",
};
