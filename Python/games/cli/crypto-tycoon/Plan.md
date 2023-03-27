# Crypto Tycoon Game 

## MoSCoW

### Must have 
- Money (Accounts)
- Assets (Crypto Coins)
- Stock Exchange (Markets)

### Should have
- A help page (User Guide)
- Test Cases
- Documentation
- Database (SQLalchemy)

### Could have 
- Get live prices from a real crypto exchange
- Settings: To change how the game behaves.

### Won't have 
- Graphical User Interface (GUI)

## Classes and Structure

### Assets 
- AssetType
- AssetPrice (Tied to market)

#### Types
-  btc (Bitcoin)
-  xmr (Monero)
-  eth (Etherium)

### Account 
- Account Holder
- Balance
- AquiredAssets
- Turns

### Stock Market 
- Assets (Type of asset)
- Price of assets