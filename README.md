Configure an ECS task definition with the following parameters:

* Environment variable `WAIT_SECONDS`: `60`
* Environment variable `GRACE_PERIOD`: `180`
* Container healthcheck: `CMD-SHELL, /var/health.sh`
* Platform: `EC2`
* Networking mode: `awsvpc`

Then the ECS service:

* ALB check grace period: `70` (add some margin over the 60 seconds of startup time)

And the ALB target group:

* Health checks: as quick as possible to `/` on traffic port (8000)
* Slow start: `180`

Start two terminals. In one, log into the EC2 instance hosting the containers and run:

```
while true; do docker ps; sleep 5; done
```

In the other one, run this locally;

```
while true; do echo "$(date) - - - $(curl -v <YOUR ALB DNS> 2>&1 | grep -i X-App)"; sleep 1; done
``

The response headers include the IP of the container network interface. You'll see that the container starts and receives no traffic during the first minute, and during the next three minutes it receives traffic in an increasing manner. After three minutes, the Docker health check will go into `healthy` and ECS will remove the old container and stop the task.
