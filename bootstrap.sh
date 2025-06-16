# automates creating a venv
# activates venv
# installs dependencies from requirements



# Step 1: Create virtual environment
echo "🟢 Creating virtual environment..."
python3 -m venv venv

# Step 2: Activate it
echo "🟡 Activating virtual environment..."
source venv/bin/activate

# Step 3: Install dependencies
echo "🔵 Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Success message
echo "✅ Environment ready!"
