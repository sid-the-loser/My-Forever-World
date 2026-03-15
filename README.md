![World Icon](icon.png) 

# My Forever World

This is the Minecraft world that I play on all the time. So, why not version control it! 

Here are all the screenshots that I manually sync between devices: [screenshots.md](screenshots/screenshots.md)

PS. This also helps me sync between devices.

PPS. The code I use to commit my updates:

```bash
current_time=$(date +"%Y-%m-%d %H:%M:%S")

cd ~/.minecraft/saves/My-Forever-World
git pull
git add .
git commit -m "${current_time}"
git push
```
