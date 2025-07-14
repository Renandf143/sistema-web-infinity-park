
import express from 'express';
import { spawn } from 'child_process';
import path from 'path';

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware para servir arquivos estáticos
app.use(express.static('public'));

// Função para iniciar o Django
function startDjango() {
  console.log('🎢 Iniciando servidor Django do Infinity Park...');
  
  const djangoPath = path.join(__dirname, '../InfinityPark/WebMola/InfinityPark/DjangoHelloWorld');
  
  // Primeiro, configurar o sistema
  const configProcess = spawn('python', ['configurar_infinity_park.py'], {
    cwd: djangoPath,
    stdio: 'inherit',
    shell: true
  });
  
  configProcess.on('close', (code) => {
    if (code === 0) {
      console.log('✅ Sistema configurado com sucesso!');
      
      // Agora iniciar o servidor Django
      const djangoProcess = spawn('python', ['manage.py', 'runserver', '0.0.0.0:5000'], {
        cwd: djangoPath,
        stdio: 'inherit',
        shell: true
      });
      
      djangoProcess.on('error', (error) => {
        console.error('❌ Erro ao iniciar Django:', error);
      });
      
      console.log('🚀 Infinity Park Django rodando na porta 5000');
      console.log('🌐 Acesse: http://localhost:5000');
    } else {
      console.error('❌ Erro na configuração do sistema');
    }
  });
}

// Iniciar Django automaticamente
startDjango();

// Rota de fallback para redirecionar para o Django
app.get('*', (req, res) => {
  res.redirect('http://localhost:5000');
});

app.listen(PORT, () => {
  console.log(`🌐 Servidor proxy rodando na porta ${PORT}`);
});
