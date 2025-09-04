# Reliable Web Demo!

Learning the ins and outs of setting up Kubernetes
objects. I'm aware of these concepts, but have 
never truly implemented them on my own. This 
is my jab at doing so!

# Day 1 (02/09/2025) - Setup
Pretty much just worked on setting up a basic Flask 
server, getting the Docker image created, and running 
a Kubernetes Cluster in my local machine (via
Docker Desktop). Began templating out the deployment 
and service, which fortunately worked fine. 

Had to figure out what the metadata and labels really 
meant, as well as how they connect between 
deployment and service (and eventually other objs).
Also needed to refresh my memory on ports and 
service types. For now, using NodePort.

# Day 2 (03/09/2025) - Ingress
To better reflect how things work might work IRL,
I'm going to use a ClusterIP Service with Ingress
rules. 

This was my first time doing anything with nginx.
Installed it via YAML manifest instead of Helm for 
simplicity. Ran into some initial issues with 
the spec, turns out ingressClassName is important.
Managed to get the pathing working as expected.

Also added a livenessProbe. Saw it working as 
expected here!
![LivenessProbeLogs](/imgs/day2-liveness.png)

# Day 3 (04/09/2025) - Prometheus
https://spacelift.io/blog/prometheus-kubernetes#why-use-prometheus-for-kubernetes-monitoring

https://spacelift.io/blog/prometheus-operator 

Learning what Promethus is and how to implement it
into everything. Used the API Client in my flask app
and things seem to be working (ran into a small 
issue where it said the address was already in use, 
but that was because Flask debug mode reloads the
code when the server is up, which also calls the 
Promethus server start again!). Also, to make things 
easier, I changed the Service back to a NodePort.

![Prometheus metrics in app](/imgs/day3%20-%20flask%20metrics.png)

I then proceeded to work on configuring a prometheus
Service and Service Monitor. It took me a while 
to figure out that the `name` for the ports had to
match. I wasn't quite sure what that field was 
in the first place. It wasn't clear to me that 
the ServiceMonitor specifically looked for that.
Got it to work and was able to view things through 
Prometheus UI and Grafana. Getting used to 
Grafana dashboards may still take a minute...

![Prometheus UI metrics](/imgs/day3%20-%20prometheus%20ui%20metrics.png)
![Grafana Dashboard](/imgs/day3%20-%20grafana%20metrics.png)

I even took a jab at deleting a pod, just to see 
what the response was for everything. K8s kept its 
cool and so did all the monitoring!

![Grafana after Pod deletion](/imgs/day3%20-%20grafana%20metrics%202.png)
