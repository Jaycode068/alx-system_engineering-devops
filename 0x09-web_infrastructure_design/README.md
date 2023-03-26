# 0x09. Web infrastructure design

## Overview:

The web infrastructure consists of multiple components that work together to deliver a web application to users over the internet. The application is hosted on a set of servers that are connected to a load balancer, which distributes incoming traffic evenly across the servers. The infrastructure is designed to be scalable, secure, and reliable, with redundant components to minimize the risk of downtime.

## Components:
The web infrastructure consists of the following components:

## Web Server:

Web Server: A web server is responsible for serving static content like HTML, CSS, and images to users. The web server used in this design is Nginx, a popular open-source web server known for its high performance and low resource usage.

## Application Server:

Application Server: An application server is responsible for running the application code and generating dynamic content for users. The application server used in this design is Apache Tomcat, a popular open-source application server that supports Java-based applications.

## Load Balancer:

Load Balancer: A load balancer distributes incoming traffic evenly across multiple servers, helping to improve performance and prevent overloading any one server. The load balancer used in this design is HAProxy, a popular open-source load balancing software.

## Database:

Database: The database is used to store and retrieve data for the application. The database used in this design is MySQL, a popular open-source relational database management system. MySQL is used to store and retrieve data for the website, including user accounts, settings, and content. The code base contains the website code and assets, including HTML, CSS, JavaScript, images, and other media. The SSL certificate is used to secure the website by encrypting traffic between the user's browser and the web server.

## Firewall:

Firewall: Firewalls are used to protect the infrastructure from unauthorized access and attacks. The infrastructure has three firewalls that are configured to restrict incoming and outgoing traffic to the necessary ports and protocols.

## Monitoring:

The monitoring system is used to collect and analyze server metrics and logs, such as CPU usage, memory usage, disk space, network traffic, and website response time. This information is used to troubleshoot issues, identify performance bottlenecks, and optimize the infrastructure for better performance and reliability.


## Domain Name:

The domain name is used to identify the web application on the internet. In this design, the domain name used is `www.foobar.com`. A domain name is important because it provides a human-readable name that users can remember and use to access the application. The domain name is registered with a domain registrar like GoDaddy or Namecheap, which assigns it to an IP address.

## DNS Record:

The www in `www.foobar.com` is a subdomain, which is used to identify a specific part of the domain. In this design, the www subdomain is a CNAME record, which points to the domain name of the load balancer. This allows users to access the web application by entering the www subdomain in their browser.

## Communication:

When a user requests the web application, the web server and application server work together to generate the content, which is then sent back to the user's computer over the internet. The communication between the user's computer and the servers is done using HTTP and HTTPS protocols.

## Issues:

There are several potential issues with this web infrastructure design, including:

`SPOF`:
	To solve the issue of a single point of failure (SPOF), we can add redundancy to the critical components of the infrastructure. For example, we can have multiple web servers, application servers, load balancers, and databases running in parallel, so that if one component fails, the other components can take over seamlessly.

`Downtime when maintenance needed:`
	To avoid downtime when maintenance is required, we can use techniques such as rolling updates or blue-green deployments, which allow us to update the infrastructure without interrupting the service. In rolling updates, we update one server at a time, while the others keep serving requests. In blue-green deployments, we have two identical infrastructures, one active and one inactive. We update the inactive one, and then switch the traffic to it once it's ready.

`Cannot scale if too much incoming traffic:`
	To handle a large volume of incoming traffic, we can scale our infrastructure horizontally by adding more web servers, application servers, and databases. We can also use auto-scaling to automatically add or remove resources based on the current demand.

`Security issues (no firewall, no HTTPS):`
	To address security issues, we can add firewalls to restrict access to the infrastructure and HTTPS to encrypt the traffic between the server and the user's browser.

`No monitoring:`
	To ensure the reliability and performance of the infrastructure, we need to set up monitoring to track metrics such as CPU usage, memory usage, network traffic, and error rates. This can help us detect issues before they become critical and allow us to take proactive measures.

`Why terminating SSL at the load balancer level is an issue:`
	Terminating SSL at the load balancer level means that the traffic between the load balancer and the web servers is not encrypted. If someone intercepts the traffic between the load balancer and the web servers, they can see the sensitive information in plain text. To solve this issue, we can use end-to-end encryption by configuring SSL on each web server.

`Why having only one MySQL server capable of accepting writes is an issue:`
	Having only one MySQL server capable of accepting writes can lead to a single point of failure and reduce the performance of the application. To solve this issue, we can set up a master-slave replication, where the master database handles writes, and the slave databases handle reads. This can improve the performance and reliability of the application.

`Why having servers with all the same components (database, web server, and application server) might be a problem:`
	Having servers with all the same components can lead to a single point of failure, make it difficult to troubleshoot issues, and limit the scalability of the infrastructure. To solve this issue, we can separate the components into different servers, which allows us to scale each component independently, reduces the impact of failures, and makes it easier to troubleshoot issues.

## Conclusion:

In conclusion, designing a web infrastructure requires careful consideration of various components and factors such as scalability, redundancy, security, and monitoring. A well-designed web infrastructure can provide high availability and performance for users, while a poorly designed one can result in downtime, slow response times, and security vulnerabilities. To avoid these issues, it is important to consider implementing redundant components, load balancing, firewalls, SSL encryption, and monitoring tools. It is also crucial to address potential issues such as single points of failure, lack of scalability, and security vulnerabilities. By taking these factors into account and designing a robust infrastructure, websites can provide a seamless user experience while ensuring security, reliability, and scalability.

