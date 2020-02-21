
#
# @lc app=leetcode id=71 lang=ruby
#
# [71] Simplify Path
#

# @lc code=start
# @param {String} path
# @return {String}
def simplify_path(path)
  list_path = path.split('/').select {|it| it != "" and it != "."}

  Array result = []
  print("List path: ", list_path)
  list_path.each{ |x| 
    if x == ".."
        result.pop()
    else
        result.push(x)
    end
  }
  return "/" + result.join("/")
end
# @lc code=end
# result = simplify_path("/a/./b/../../c/")
result = simplify_path("/a//b////c/d//././/..")
puts("result: ", result)
