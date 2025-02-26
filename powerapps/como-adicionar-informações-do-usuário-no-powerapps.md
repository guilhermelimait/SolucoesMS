# Como adicionar informações do usuário no PowerApps

Date: 2021-06-15 12:37:11

Categories: PowerApps

---

<p>Para adicionar, basta adicionar o conector Microsoft 365 ao seu app e utilizar esses comandos no campo Text do objeto que está utilizando:</p>
<p><strong>Nome:</strong> Office365Users.MyProfile().GivenName</p>
<p><strong>Sobrenome:</strong> Office365Users.MyProfile().Surname</p>
<p><strong>Email</strong>: Office365Users.MyProfile().Email</p>
<p><strong>Foto:</strong> Office365Users.UserPhoto(Office365Users.MyProfile().Id)</p>
<p>Até mais!<br />
<a href="https://docs.microsoft.com/pt-br/powerapps/maker/canvas-apps/functions/function-user">Fonte1</a>, <a href="https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/connections/connection-office365-users">Fonte2</a></p>
