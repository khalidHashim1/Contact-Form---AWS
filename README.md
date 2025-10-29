## Contact Form Submission Workflow

This project shows a serverless contact form using **AWS Lambda**, **API Gateway**, **DynamoDB**, and **Amazon SES**.

### 1. Frontend HTML Form
- User fills out a contact form (`name`, `email`, `message`).
- Form sends the data as JSON to an **API Gateway endpoint**.

### 2. API Gateway
- Receives the form data from the frontend.
- Calls the **Lambda function** with the data.

### 3. AWS Lambda Function
- Receives the form data and does the following:
  1. Creates a unique `id` for each submission.
  2. Adds a timestamp (`submittedAt`).
  3. Stores the data in **DynamoDB**.
  4. Sends an email with the submission details using **SES**.
- Returns a success or error message to the frontend.

### 4. DynamoDB
- Table: `ContactFormSubmissions`
- Stores all submissions with:
  - `id` (unique ID)
  - `name`
  - `email`
  - `message`
  - `submittedAt` (timestamp)

### 5. Amazon SES
- Sends an email notification for every submission.
- Keeps the site owner informed in real-time.
- **Important:** Emails sent via SES can sometimes go to Gmail's Spam folder.  
  To avoid this, create a filter in Gmail to automatically mark these emails as “Not Spam” or move them to your inbox.

---

**Technologies Used:**  
- AWS Lambda (serverless backend)  
- API Gateway (connects frontend with Lambda)  
- DynamoDB (store submissions)  
- Amazon SES (email notifications)  
- Python (Lambda function)  
