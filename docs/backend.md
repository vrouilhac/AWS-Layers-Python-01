# Backend

## Api Endpoints

<details>
<summary><strong>/tasks</strong></summary>

```yaml
GET: Retreive all user's tasks
POST: Add a user's task
```

</details>

<details>
<summary><strong>/tasks/{taskId}</strong></summary>

```yaml
GET: Retreive a single user's task
PUT: Update a user's task 
DELETE: Delete a user's task
```

</details>

All endpoints can be called using postman. A collection is available in the repository.

## Database

The database is DynamoDB with single table design pattern.

### User

| Attribute name | Type | DB Name		 |
| -------------- | ---- | ---------- |
| id						 | S		| PK				 |
| SK						 | S		| SK				 |
| email					 | S		| label			 |
| username			 | S		| username	 |

### Task

| Attribute name | Type | DB Name		 |
| -------------- | ---- | ---------- |
| id						 | S		| PK				 |
| label					 | S		| label			 |
| done					 | BOOL	| done			 |
| created_at		 | S		| SK				 |
| updated_at		 | N		| updated_at |

## Database Query

| Query																		| Index			| Params																|
| --------------------------------------- | --------- | ------------------------------------- |
| Get user by userId											| Table			|	`PK = userId`													|
| Get user tasks													| Table			| `PK = userId & SK begin_with TASK`		|
| Get user task by userId and taskId			| Table			| `PK = userId & SK = TASK::<taskId>`		|


