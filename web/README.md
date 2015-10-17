# redirekter

Free HTTP redirects for your service.
With stateless servers and all you are seldom in the control of the load balancer
and it is no longer as easy to configure HTTP redirects.

**redirekter** is a free service to answer to Requests.

Use Cases:

- Redirect from `domain.com` to `www.domain.com`
- Redirect `company.ch` to `company.com/switzerland`

## Architecture

- **etcd** backed configuration store
- Management portal which writes into **etcd**
- Nginx config get's rewritten on nginx change
  - Problem: Many config reloads, security injects
  - How to deal with invalid configs
- Or custom Golang server which reads the data from etcd -> how to cache?

Portal needs to provide a way to map urls to other urls and choose the status code.

Listen on etcd key change and then update in-memory structure.
Each request reads from the in-memory structure the domains and wished redirects.


## How much time


