# MailBomber

<div align="center">
  <img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/5b6500eb-6ca4-4644-a6c2-9fb19bd811ae" width="170px">
</div>
<br>

Tool developed in Python, which allows to carry out email spamming attacks in an effective and simple way. This script uses the Gmail email service to send multiple emails to a specific email address.

## Requirements

1. Verify that you have all the necessary modules installed using the command:

```
pip3 install -r requeriments.txt
```

2. Before running the script it is crucial to have an "application password" generated for your email account. This is necessary to allow the script to send emails on your behalf without compromising your main account password.

### Steps to Create an Application Password (Gmail)

1. **Sign in to your Gmail account:** Make sure you are logged in to the account from which you want to send emails.

<img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/d02cb09f-0042-4350-8884-da66ee4909d2" width="400px">

2. **Access the Security Settings:** Go to your Google account security settings. You can do this from [Google Account Settings](https://myaccount.google.com/).

![imagen](https://github.com/0xJuaNc4/MailStorm/assets/130152767/833498eb-9604-4a26-b33f-b83046c1dee1)

3. **Enable Two-Step Verification:** If you have not enabled two-step verification, you will be prompted to do so. Follow the instructions to set up this additional level of security.

<div align="center">
<img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/b1ee1be6-f1d5-4484-84f0-60c0354cee32" width="650px">
</div>

4. **Generate Application Password:** In the "Application Passwords" section, choose "Select Application" and "Other (custom name)". Then click "Generate".

<img src="https://github.com/0xJuaNc4/MailBomber/assets/130152767/96b13b0a-4ee4-44d9-ae45-ae160227d678" width="500px">

5. **Copy the Generated Password:** You will be provided with a specific password for the application. Copy this password, as you will need it when running the script.

<img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/eb95df5e-93eb-4e78-96da-b17b60f0a902" width="500px">


## Usage

Clone the repository:
```
git clone https://github.com/tuusuario/MailBomber
```
Enter the project directory:
```
cd MailBomber
```
Execute the script:
```
python mailbomber.py
```
