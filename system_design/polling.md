# Long Polling / WebSockets / Server Sent

Communication protocols between clients and server.

## Ajax Polling

Clent repeatedly polls / requests server for data. If no data, return empty response.

Problem is client keep asking server for new data. Many empty response are returned creating HTTP overhead.

## Long Polling

Hanging GET.

If the server dies not have new data, instead of sending empty response, holds the request till data is available unless timeout. The client immediately re-request after receiving the new data.

## WebSockets

Full duplex communication, persistent connection, real time transfer.

## Server Sent Events (SSEs)

Persistent and long term from server to client.