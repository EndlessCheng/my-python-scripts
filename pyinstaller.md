# 命令

虽然 `main.py` 可以直接不加包名地 import 所在目录中的其他 .py 文件，但是 pyinstaller 无法识别这一点，所以我们需要 `cd` 到 `main.py` 所在目录。

  * 非虚拟环境，使用 `$ pyinstaller -F main.py`
  * 虚拟环境下，使用 `$ xxx_env/bin/pyinstaller -F main.py`


# 准备工作

1. （虚拟环境下）确保 pyinstaller 安装在虚拟环境的三方库中。

2. 确认 distribute setuptools 均已安装且为最新版本。


# 源码修改

1. Exception: Versioning for this project requires either an sdist tarball, or access to an upstream git repository. It's also possible that there is a mismatch between the package name in setup.cfg and the argument given to pbr.version.VersionInfo. Project name mock was given, but was not able to be found.

  解决：在 `mock/mock.py` 中，71-73 行修改成：
  ```
  # _v = VersionInfo('mock').semantic_version()
  __version__ = '2.0.0'  # _v.release_string()
  version_info = (2, 0, 0, 'final', 0)  # _v.version_tuple()
  ```
  
2. 无法找到 APScheduler。

  解决：修改 `apscheduler/__init__.py` 的 `release = ...` 为 `release = '3.3.1'`（具体版本号请用 Python 终端获取）


# summer 项目

1. 移动 `resource` 目录到 `~` 目录下。

2. 修改获取资源文件路径的代码，即修改 `hh_online/parameters/parameter.py` 中的 `RESOURCE_ROOT_DIRECTORY = os.path.join(os.path.expanduser('~'), 'resource')`


# Django

1. 查看项目文件夹名和 `settings.py` 所在文件夹名是否*不同名*，如果*同名*则修改项目文件夹名。

2. 项目根目录下添加空的 `__init__.py` 文件。

3. `manage.py` 中添加：
  ```
  def load_modules():
      from django.conf import settings
  
      from caroline import settings, urls, wsgi
  ```
  
4. 资源路径修改：

`settings.py` 修改内容：
  ```
  UPLOAD_DIR = os.path.join(os.path.expanduser('~'), 'static')

  STATICFILES_DIRS = [
      os.path.join(os.path.expanduser('~'), 'static'),  # os.path.expanduser('~'),
      os.path.join(BASE_DIR, 'server_project/static')
  ]
  ```
  
`urls.py` 修改内容：
  ```
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
  ```
  
5. `settings.py` 末尾添加：
  ```
  TEMPLATE_CONTEXT_PROCESSORS = []
  TEMPLATE_LOADERS = []
  ```
  
6. 若在打包时有“错误的语法”这样的异常，请检查项目中相应输出的位置，并注释掉相关的 `print` 语句。（此处为 pyinstaller 的缺陷）


# 第三方库报错

1. tensorflow：`sudo gedit /etc/environment` 添加一行 `PBR_VERSION=3.1.1`（可以用 `pbr -v` 查看版本号）


# 附

* [If Things Go Wrong](https://github.com/pyinstaller/pyinstaller/wiki/If-Things-Go-Wrong)
