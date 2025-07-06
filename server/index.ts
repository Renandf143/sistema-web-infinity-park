import { spawn } from 'child_process';
import path from 'path';

const PORT = 5000;

// Diretório do projeto Django
const DJANGO_DIR = path.join(process.cwd(), 'InfinityPark', 'WebMola', 'InfinityPark', 'DjangoHelloWorld');

let djangoProcess: any = null;

// Função para iniciar o Django diretamente na porta 5000
function startDjango() {
  console.log('🎢 Iniciando servidor Django do Infinity Park...');
  
  djangoProcess = spawn('python', ['manage.py', 'runserver', `0.0.0.0:${PORT}`], {
    cwd: DJANGO_DIR,
    stdio: 'inherit'
  });

  djangoProcess.on('error', (err: any) => {
    console.error('Erro ao iniciar Django:', err);
  });

  djangoProcess.on('close', (code: any) => {
    console.log(`Django finalizado com código: ${code}`);
  });
}

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('Finalizando servidor...');
  if (djangoProcess) {
    djangoProcess.kill();
  }
  process.exit(0);
});

process.on('SIGINT', () => {
  console.log('Finalizando servidor...');
  if (djangoProcess) {
    djangoProcess.kill();
  }
  process.exit(0);
});

// Iniciar Django
startDjango();

console.log(`🚀 Infinity Park Django rodando na porta ${PORT}`);
console.log(`🌐 Acesse: http://localhost:${PORT}`);