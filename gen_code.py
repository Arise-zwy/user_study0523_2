# 定义视频链接列表


import glob


# 自定义名字顺序映射
name_order = {
    'art_Shutterstock1c_ani.png': -1,
    'reference': 0,
    'ours': 1,
    'LIA': 2,
    'PIR': 3,
    'MRAA':4,
    'FOMM':5,
    # 添加更多名字和对应的顺序...
}


# 自定义排序函数
def custom_sort(item):
    return name_order.get(item, float('inf'))

def sort_by_first_letter(path):
    file_name = path.split('\\')[-1]  # 获取最后一个文件名
    return custom_sort(file_name.split(" ")[0])  # 返回首字母的小写形式进行排序



video_list1=glob.glob("C:/Users/WY/Desktop/user_study_demo/user_study/*")
video_list2=glob.glob("C:/Users/WY/Desktop/user_study_demo/user_study_exp/*")

video_all={}
input_all={}
for i in range(len(video_list1)-1):
    video_path=glob.glob(video_list1[i]+"/*.mp4")
    png_path=glob.glob(video_list1[i]+"/*.png")

    new_path=[]
    for j in range(len(video_path)):
        new_path.append(video_path[j])
    video_all[video_list1[i].split("\\")[-1]]=new_path
    input_all[video_list1[i].split("\\")[-1]]=png_path

video_all2={}
input_all2={}

for i in range(len(video_list2)-1):
    video_path=glob.glob(video_list2[i]+"/*.mp4")
    png_path=glob.glob(video_list2[i]+"/*.png")

    new_path=[]
    for j in range(len(video_path)):
        new_path.append(video_path[j])
    video_all2[video_list2[i].split("\\")[-1]]=new_path
    input_all2[video_list2[i].split("\\")[-1]]=png_path



# 生成HTML代码
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>user_study</title>
    <style>
    body {
      text-align: center; /* 居中文本 */
    }
    h1 {
      font-size: 48px; /* 设置标题字体大小 */
    }
    .line-break {
    margin-bottom: 40px;
    }
    </style>
</head>
<body>
    <h1>user study 1</h1>
    <h3>Our method works well on the male and female Portrait-to-Caricature Translation. The first col is input portrait video.这里需要你写描述</h3>
    <!-- <h3>Click the video to view it in high resolution.</h3> -->

    <table border="6" style="table-layout: fixed;">      <!-- 设置几个case -->

            
'''
#先列举case，然后每个case列举视频
# for i, link in enumerate(video_links, start=1):


case_id=1
for key,lis in video_all.items():
    html_code += f'''  <tr>'''
    lis.sort(key=sort_by_first_letter)
    print(key)
    html_code += f'''

            <td halign="center" style="word-wrap: break-word;" valign="top">
                <p>
                    <a>
                        <img src="{input_all[key][0]}" alt="My Image" width="200px" height="auto"> 
                    </a><br>
                    <p>Input</p>
                </p>
        </td>
        <td style="text-align: center; vertical-align: middle; word-wrap: break-word;" valign="middle">
                    <p style="color: red; font-weight: bold;font-size: 30px;">Case{case_id}</p>
                    <button onclick="playPause('C{case_id}_')">Play/Pause</button>
        </td>

    '''
    for idx,path_name in enumerate(lis):
        if idx==0:
            method_name="Reference"
        else:
            method_name="Method"+str(idx) 
        if idx==3:
            print(path_name)  
        html_code += f'''
          
                <td halign="center" style="word-wrap: break-word;" valign="top">
                    <p>
                        <a>
                            <video id='C{case_id}_{idx}' muted loop="loop" src="{path_name}" style="width: 200px; height: auto;"></video>
                        </a><br>
                        <p>{method_name}</p>
                    </p>
                </td>
        '''
    html_code += f'''  </tr>     
'''
    case_id+=1
html_code += f'''  </table>'''




'''exp2'''




html_code += ''' 
<div class="line-break"></div>

<h1>user study 2</h1>

<h3>Our method works well on the male and female Portrait-to-Caricature Translation. The first col is input portrait video.写描述 标准</h3>
<h3>  </h3>
'''
html_code += f'''      <table border="6" style="table-layout: fixed;">      <!-- 设置几个case -->'''

case_id=1
for key,lis in video_all2.items():
    html_code += f'''  <tr>'''
    lis.sort(key=sort_by_first_letter)
    print(key)
    html_code += f'''
        <td halign="center" style="word-wrap: break-word;" valign="top">
                <p>
                    <a>
                        <img src="{input_all2[key][0]}" alt="My Image" width="200px" height="auto"> 
                    </a><br>
                    <p>Input</p>
                </p>
        </td>
        <td style="text-align: center; vertical-align: middle; word-wrap: break-word;" valign="middle">
                    <p style="color: red; font-weight: bold;font-size: 30px;">Case{case_id}</p>
                    <button onclick="playPause('C{case_id}_')">Play/Pause</button>
        </td>

    '''
    for idx,path_name in enumerate(lis):
        if idx==0:
            method_name="Reference"
        else:
            method_name="Method"+str(idx) 
        if idx==3:
            print(path_name)  
        html_code += f'''
          
                <td halign="center" style="word-wrap: break-word;" valign="top">
                    <p>
                        <a>
                            <video id='C{case_id}_{idx}' muted loop="loop" src="{path_name}" style="width: 200px; height: auto;"></video>
                        </a><br>
                        <p>{method_name}</p>
                    </p>
                </td>
        '''
    html_code += f'''  </tr>'''
    case_id+=1

html_code += f'''  </table>'''















html_code += '''
    </table>

    <script>
        function playPause(name) {
            for (var i = 1; i <= 7; i++) {
                var myVideo = document.getElementById(name + i);
                if (myVideo.paused)
                    myVideo.play();
                else
                    myVideo.pause();
            }
        }
    </script>

</body>
</html>
'''

# 将生成的HTML代码写入文件
with open('video_gallery.html', 'w') as file:
    file.write(html_code)
