from setuptools import setup, find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(
    name='TweetMood-Monitor',
    description="Package that streams Twitter feed and anaylise for sentiment and bullying via a streamlit dashboard",
    packages=find_packages(),  # It will find all packages in your directory
    install_requires=requirements,
    version='0.0.1'
)
