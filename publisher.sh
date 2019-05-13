#!/usr/bin/env bash
echo "正在打包....."
python3 setup.py sdist bdist_wheel

echo "正在发布，过程需要提供账户和密码......"
twine upload dist/*
echo "正在清理发布产生的目录信息......"
rm -rf build dist
echo "发布完成!"