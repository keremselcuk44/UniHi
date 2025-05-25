const express = require('express')
const { exec } = require('child_process')
const app = express()

app.use(express.json())

app.post('/webhook', (req, res) => {
  if (req.body.ref === 'refs/heads/main') {  // main branch ise
    exec('cd /home/ubuntu/UniHi/backend && git pull && pm2 restart unihi-backend', (err, stdout, stderr) => {
      if (err) {
        console.error('Deploy error:', err)
        return res.status(500).send('Deploy failed')
      }
      console.log('Deploy output:', stdout)
      res.send('Deploy success')
    })
  } else {
    res.status(400).send('Wrong branch')
  }
})

app.listen(3000, () => console.log('Webhook listener started on port 3000'))
