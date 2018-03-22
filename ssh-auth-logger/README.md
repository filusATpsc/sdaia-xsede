Docker container for ssh-auth-logger.

See https://github.com/JustinAzoff/ssh-auth-logger

To test:

```
docker run -d --network ... --env "SSHD_BIND=:2222" -h ssh-auth-logger -p 2222:2222 --name ssh-auth-logger ssh-auth-logger
```
