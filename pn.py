if _G.Ran == true then return end
wait()
_G.Ran = true
repeat wait() until game:IsLoaded()
local Stats = game:GetService("Stats")
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TweenService = game:GetService("TweenService")
local speedFactorPingBased
local speedFactor
local Nurysium_Util = loadstring(game:HttpGet("https://raw.githubusercontent.com/flezzpe/Nurysium/main/nurysium_helper.lua"))()
local function getTrainingBall()
	for index, ball in workspace:WaitForChild("TrainingBalls"):GetChildren() do
		if ball:IsA("BasePart") and ball:GetAttribute("realBall") then
			return ball
		end
	end
end
local ismyautoparryspamming
local local_player = Players.LocalPlayer
local camera = workspace.CurrentCamera
local standalone = false
print("Crate By Lunar(break) & CodeE4X")

local originalParryRemote
local originalResolveParryRemote 
local aivar, visualizervar, autospamvar, autoparryvar, tphitvar, autowinvar
local nurysium_Data = nil
local hit_Sound = nil
local closest_Entity = nil
local aura_Enabled = false
local auto_curve = false
local auto_spam = false
local training_mode = false
local anti_curve_spam_Enabled = false
local visualize_Enabled = false
local ai_Enabled = false
local auto_win = false
local tp_hit = false
local potanum = 15
local Services = {game:GetService("AdService"),game:GetService("SocialService")}

local function get_closest_entity(Object)
	task.spawn(function()
		local closest
		local max_distance = math.huge
		for index, entity in workspace.Alive:GetChildren() do
			if entity.Name ~= Players.LocalPlayer.Name then
				local distance = (Object.Position - entity.HumanoidRootPart.Position).Magnitude
				if distance < max_distance then
					closest_Entity = entity
					max_distance = distance
				end
			end
		end
		return closest_Entity
	end)
end

function resolve_parry_Remote()
 local temp_remote = game:GetService("VirtualUser"):WaitForChild("\n\n\n\n\n")

    if not temp_remote then
        return
    end

    if not temp_remote:IsA('RemoteEvent') then
        return
    end

    originalParryRemote = temp_remote
end

resolve_parry_Remote()

function walk_to(position)
	local_player.Character.Humanoid:MoveTo(position)
end
local function get_center()
	for _, object in workspace.Map:GetDescendants() do
		if object.Name == 'BALLSPAWN' then
			return object
		end
	end
end

local function linear_predict(a: number, b: number, time_volume: number)
    time_volume = math.clamp(time_volume, 0, 1)

    return a + (b - a) * time_volume
end


local aura_table = {
	canParry = true,
	is_Spamming = false,
	parry_Range = 31,
	spam_Range = 0,  
	hit_Count = 0,
	hit_Time = tick(),
	ball_Warping = tick(),
	is_ball_Warping = false,
	last_target = nil,
}

workspace:WaitForChild("Balls").ChildRemoved:Connect(function(child)
	aura_table.hit_Count = 0
	aura_table.is_ball_Warping = false
	aura_table.is_Spamming = false
	aura_table.canParry = true
	aura_table.last_target = nil
end)

ReplicatedStorage.Remotes.ParrySuccessAll.OnClientEvent:Connect(function()
	aura_table.hit_Count += 1

	task.delay(0.185, function()
		aura_table.hit_Count -= 1
	end)
end)

-- Call resolve_parry_Remote once to initialize the originalParryRemote

--start, the real one

local MauaulSpam -- Declare MauaulSpam globally

function ManualSpam()
    -- Gui to Lua
    -- Version: 3.2
    
    if MauaulSpam then
        MauaulSpam:Destroy()
        MauaulSpam = nil
        return
    end

    MauaulSpam = Instance.new("ScreenGui")
    MauaulSpam.Name = "MauaulSpam"
    MauaulSpam.Parent = game.CoreGui
    MauaulSpam.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
    MauaulSpam.ResetOnSpawn = false

    local Main = Instance.new("Frame")
    Main.Name = "Main"
    Main.Parent = MauaulSpam
    Main.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
    Main.BorderColor3 = Color3.fromRGB(0, 0, 0)
    Main.BorderSizePixel = 0
    Main.Position = UDim2.new(0.41414836, 0, 0.404336721, 0)
    Main.Size = UDim2.new(0.227479532, 0, 0.191326529, 0)

    local UICorner = Instance.new("UICorner")
    UICorner.Parent = Main

    local IndercantorBlahblah = Instance.new("Frame")
    IndercantorBlahblah.Name = "IndercantorBlahblah"
    IndercantorBlahblah.Parent = Main
    IndercantorBlahblah.BackgroundColor3 = Color3.fromRGB(255, 0, 0)
    IndercantorBlahblah.BorderColor3 = Color3.fromRGB(0, 0, 0)
    IndercantorBlahblah.BorderSizePixel = 0
    IndercantorBlahblah.Position = UDim2.new(0.0280000009, 0, 0.0733333305, 0)
    IndercantorBlahblah.Size = UDim2.new(0.0719999969, 0, 0.119999997, 0)

    local UICorner_2 = Instance.new("UICorner")
    UICorner_2.CornerRadius = UDim.new(1, 0)
    UICorner_2.Parent = IndercantorBlahblah

    local UIAspectRatioConstraint = Instance.new("UIAspectRatioConstraint")
    UIAspectRatioConstraint.Parent = IndercantorBlahblah

    local PC = Instance.new("TextLabel")
    PC.Name = "PC"
    PC.Parent = Main
    PC.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
    PC.BackgroundTransparency = 1.000
    PC.BorderColor3 = Color3.fromRGB(0, 0, 0)
    PC.BorderSizePixel = 0
    PC.Position = UDim2.new(0.547999978, 0, 0.826666653, 0)
    PC.Size = UDim2.new(0.451999992, 0, 0.173333332, 0)
    PC.Font = Enum.Font.Unknown
    PC.Text = "PC: E to spam"
    PC.TextColor3 = Color3.fromRGB(57, 57, 57)
    PC.TextScaled = true
    PC.TextSize = 16.000
    PC.TextWrapped = true

    local UITextSizeConstraint = Instance.new("UITextSizeConstraint")
    UITextSizeConstraint.Parent = PC
    UITextSizeConstraint.MaxTextSize = 16

    local UIAspectRatioConstraint_2 = Instance.new("UIAspectRatioConstraint")
    UIAspectRatioConstraint_2.Parent = PC
    UIAspectRatioConstraint_2.AspectRatio = 4.346

    local IndercanotTextBlah = Instance.new("TextButton")
    IndercanotTextBlah.Name = "IndercanotTextBlah"
    IndercanotTextBlah.Parent = Main
    IndercanotTextBlah.Active = false
    IndercanotTextBlah.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
    IndercanotTextBlah.BackgroundTransparency = 1.000
    IndercanotTextBlah.BorderColor3 = Color3.fromRGB(0, 0, 0)
    IndercanotTextBlah.BorderSizePixel = 0
    IndercanotTextBlah.Position = UDim2.new(0.164000005, 0, 0.326666653, 0)
    IndercanotTextBlah.Selectable = false
    IndercanotTextBlah.Size = UDim2.new(0.667999983, 0, 0.346666664, 0)
    IndercanotTextBlah.Font = Enum.Font.GothamBold
    IndercanotTextBlah.Text = "Spam"
    IndercanotTextBlah.TextColor3 = Color3.fromRGB(255, 255, 255)
    IndercanotTextBlah.TextScaled = true
    IndercanotTextBlah.TextSize = 22.000
    IndercanotTextBlah.TextWrapped = true

    local UIGradient = Instance.new("UIGradient")
    UIGradient.Color = ColorSequence.new{ColorSequenceKeypoint.new(0.00, Color3.fromRGB(0, 0, 0)), ColorSequenceKeypoint.new(0.75, Color3.fromRGB(255, 0, 4)), ColorSequenceKeypoint.new(1.00, Color3.fromRGB(0, 0, 0))}
    UIGradient.Parent = IndercanotTextBlah

    local UITextSizeConstraint_2 = Instance.new("UITextSizeConstraint")
    UITextSizeConstraint_2.Parent = IndercanotTextBlah
    UITextSizeConstraint_2.MaxTextSize = 52

    local UIAspectRatioConstraint_3 = Instance.new("UIAspectRatioConstraint")
    UIAspectRatioConstraint_3.Parent = IndercanotTextBlah
    UIAspectRatioConstraint_3.AspectRatio = 3.212

    local UIAspectRatioConstraint_4 = Instance.new("UIAspectRatioConstraint")
    UIAspectRatioConstraint_4.Parent = Main
    UIAspectRatioConstraint_4.AspectRatio = 1.667

--Properties:

MauaulSpam.Name = "MauaulSpam"
MauaulSpam.Parent = game.CoreGui
MauaulSpam.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
MauaulSpam.ResetOnSpawn = false

Main.Name = "Main"
Main.Parent = MauaulSpam
Main.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
Main.BorderColor3 = Color3.fromRGB(0, 0, 0)
Main.BorderSizePixel = 0
Main.Position = UDim2.new(0.41414836, 0, 0.404336721, 0)
Main.Size = UDim2.new(0.227479532, 0, 0.191326529, 0)

UICorner.Parent = Main

IndercantorBlahblah.Name = "IndercantorBlahblah"
IndercantorBlahblah.Parent = Main
IndercantorBlahblah.BackgroundColor3 = Color3.fromRGB(255, 0, 0)
IndercantorBlahblah.BorderColor3 = Color3.fromRGB(0, 0, 0)
IndercantorBlahblah.BorderSizePixel = 0
IndercantorBlahblah.Position = UDim2.new(0.0280000009, 0, 0.0733333305, 0)
IndercantorBlahblah.Size = UDim2.new(0.0719999969, 0, 0.119999997, 0)

UICorner_2.CornerRadius = UDim.new(1, 0)
UICorner_2.Parent = IndercantorBlahblah

UIAspectRatioConstraint.Parent = IndercantorBlahblah

PC.Name = "PC"
PC.Parent = Main
PC.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
PC.BackgroundTransparency = 1.000
PC.BorderColor3 = Color3.fromRGB(0, 0, 0)
PC.BorderSizePixel = 0
PC.Position = UDim2.new(0.547999978, 0, 0.826666653, 0)
PC.Size = UDim2.new(0.451999992, 0, 0.173333332, 0)
PC.Font = Enum.Font.Unknown
PC.Text = "PC: E to spam"
PC.TextColor3 = Color3.fromRGB(57, 57, 57)
PC.TextScaled = true
PC.TextSize = 16.000
PC.TextWrapped = true

UITextSizeConstraint.Parent = PC
UITextSizeConstraint.MaxTextSize = 16

UIAspectRatioConstraint_2.Parent = PC
UIAspectRatioConstraint_2.AspectRatio = 4.346

IndercanotTextBlah.Name = "IndercanotTextBlah"
IndercanotTextBlah.Parent = Main
IndercanotTextBlah.Active = false
IndercanotTextBlah.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
IndercanotTextBlah.BackgroundTransparency = 1.000
IndercanotTextBlah.BorderColor3 = Color3.fromRGB(0, 0, 0)
IndercanotTextBlah.BorderSizePixel = 0
IndercanotTextBlah.Position = UDim2.new(0.164000005, 0, 0.326666653, 0)
IndercanotTextBlah.Selectable = false
IndercanotTextBlah.Size = UDim2.new(0.667999983, 0, 0.346666664, 0)
IndercanotTextBlah.Font = Enum.Font.GothamBold
IndercanotTextBlah.Text = "Spam"
IndercanotTextBlah.TextColor3 = Color3.fromRGB(255, 255, 255)
IndercanotTextBlah.TextScaled = true
IndercanotTextBlah.TextSize = 22.000
IndercanotTextBlah.TextWrapped = true

UIGradient.Color = ColorSequence.new{ColorSequenceKeypoint.new(0.00, Color3.fromRGB(0, 0, 0)), ColorSequenceKeypoint.new(0.75, Color3.fromRGB(255, 0, 4)), ColorSequenceKeypoint.new(1.00, Color3.fromRGB(0, 0, 0))}
UIGradient.Parent = IndercanotTextBlah

UITextSizeConstraint_2.Parent = IndercanotTextBlah
UITextSizeConstraint_2.MaxTextSize = 52

UIAspectRatioConstraint_3.Parent = IndercanotTextBlah
UIAspectRatioConstraint_3.AspectRatio = 3.212

UIAspectRatioConstraint_4.Parent = Main
UIAspectRatioConstraint_4.AspectRatio = 1.667

-- Scripts:

local function HEUNEYP_fake_script() -- IndercanotTextBlah.ColorChangeScript 
	local script = Instance.new('LocalScript', IndercanotTextBlah)

	local button = script.Parent
	local UIGredient = button.UIGradient
	local NeedToChange = script.Parent.Parent.IndercantorBlahblah
	local userInputService = game:GetService("UserInputService")
	local RunService = game:GetService("RunService")

	-- ColorSequences Ã Â¸ÂªÃ Â¸Â³Ã Â¸Â«Ã Â¸Â£Ã Â¸Â±Ã Â¸Å¡Ã Â¸ÂªÃ Â¸ÂµÃ Â¹â‚¬Ã Â¸â€šÃ Â¸ÂµÃ Â¸Â¢Ã Â¸Â§Ã Â¹ÂÃ Â¸Â¥Ã Â¸Â°Ã Â¸ÂªÃ Â¸ÂµÃ Â¹ÂÃ Â¸â€Ã Â¸â€¡
	local green_Color = {
		ColorSequenceKeypoint.new(0.00, Color3.fromRGB(0, 0, 0)), 
		ColorSequenceKeypoint.new(0.75, Color3.fromRGB(0, 255, 0)), 
		ColorSequenceKeypoint.new(1.00, Color3.fromRGB(0, 0, 0))
	}

	local red_Color = {
		ColorSequenceKeypoint.new(0.00, Color3.fromRGB(0, 0, 0)), 
		ColorSequenceKeypoint.new(0.75, Color3.fromRGB(255, 0, 0)), 
		ColorSequenceKeypoint.new(1.00, Color3.fromRGB(0, 0, 0))
	}

	local current_Color = red_Color
	local target_Color = green_Color
	local is_Green = false
	local transition = false
	local transition_Time = 1
	local start_Time

	local function startColorTransition()
		transition = true
		start_Time = tick()
	end

	RunService.Heartbeat:Connect(function()
		if transition then
			local elapsed = tick() - start_Time
			local alpha = math.clamp(elapsed / transition_Time, 0, 1)

			local new_Color = {}
			for i = 1, #current_Color do
				local start_Color = current_Color[i].Value
				local end_Color = target_Color[i].Value
				new_Color[i] = ColorSequenceKeypoint.new(
					current_Color[i].Time,
					start_Color:Lerp(end_Color, alpha)
				)
			end

			UIGredient.Color = ColorSequence.new(new_Color)

			if alpha >= 1 then
				transition = false
				current_Color, target_Color = target_Color, current_Color
			end
		end
	end)

	local function toggleColor()
		if not transition then
			is_Green = not is_Green
			if is_Green then
				target_Color = green_Color
				NeedToChange.BackgroundColor3 = Color3.new(0, 1, 0)
			else
				target_Color = red_Color
				NeedToChange.BackgroundColor3 = Color3.new(1, 0, 0)
			end
			startColorTransition()
		end
	end

	button.MouseButton1Click:Connect(toggleColor)

	userInputService.InputBegan:Connect(function(input, gameProcessed)
		if gameProcessed then return end
		if input.KeyCode == Enum.KeyCode.E then
			toggleColor()
		end
	end)

	local Services = {game:GetService("AdService"), game:GetService("SocialService")}
	local originalParryRemote = nil

	function resolve_parry_Remote()
        local temp_remote = game:GetService("VirtualUser"):WaitForChild("\n\n\n\n\n")
        if not temp_remote or not temp_remote:IsA('RemoteEvent') then
            return
        end
        originalParryRemote = temp_remote
    end

    resolve_parry_Remote()

	local camera = workspace.CurrentCamera
	local mouse = game.Players.LocalPlayer:GetMouse()

	local function getClosestEntity()
		local closest_Entity = nil
		local shortestDistance = math.huge

		for _, entity in pairs(workspace.Alive:GetChildren()) do
			if entity:IsA("Model") and entity:FindFirstChild("HumanoidRootPart") then
				local screenPoint = camera:WorldToViewportPoint(entity.HumanoidRootPart.Position)
				local distanceToMouse = (Vector2.new(screenPoint.X, screenPoint.Y) - Vector2.new(mouse.X, mouse.Y)).Magnitude

				if distanceToMouse < shortestDistance then
					closest_Entity = entity
					shortestDistance = distanceToMouse
				end
			end
		end

		return closest_Entity
	end

	RunService.RenderStepped:Connect(function()
		if is_Green and originalParryRemote then
			local closest_Entity = getClosestEntity()
			if closest_Entity then
				local cf = camera.CFrame
				local x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22 = cf:GetComponents()

				originalParryRemote:FireServer(
					0,
					CFrame.new(x, y, z, R00, R01, R02, R10, R11, R12, R20, R21, R22),
					{[closest_Entity.Name] = closest_Entity.HumanoidRootPart.Position},
					{closest_Entity.HumanoidRootPart.Position.X, closest_Entity.HumanoidRootPart.Position.Y},
					false
				)
			end
		end
	end)

	
	end
coroutine.wrap(HEUNEYP_fake_script)()
local function WWJM_fake_script() -- Main.LocalScript 
	local script = Instance.new('LocalScript', Main)

	local UserInputService = game:GetService("UserInputService")
	
	local gui = script.Parent
	local dragging
	local dragInput
	local dragStart
	local startPos
	
	local function update(input)
		local delta = input.Position - dragStart
		local newPosition = UDim2.new(
			startPos.X.Scale,
			startPos.X.Offset + delta.X,
			startPos.Y.Scale,
			startPos.Y.Offset + delta.Y
		)
	
		-- Ã Â¹Æ’Ã Â¸Å Ã Â¹â€° Tween Ã Â¹â‚¬Ã Â¸Å¾Ã Â¸Â·Ã Â¹Ë†Ã Â¸Â­Ã Â¹Æ’Ã Â¸Â«Ã Â¹â€°Ã Â¸ÂÃ Â¸Â²Ã Â¸Â£Ã Â¹â‚¬Ã Â¸â€žÃ Â¸Â¥Ã Â¸Â·Ã Â¹Ë†Ã Â¸Â­Ã Â¸â„¢Ã Â¸â€”Ã Â¸ÂµÃ Â¹Ë†Ã Â¸â€šÃ Â¸Â­Ã Â¸â€¡ Frame Ã Â¹â‚¬Ã Â¸â€ºÃ Â¹â€¡Ã Â¸â„¢Ã Â¹â€žÃ Â¸â€ºÃ Â¸Â­Ã Â¸Â¢Ã Â¹Ë†Ã Â¸Â²Ã Â¸â€¡Ã Â¸Â£Ã Â¸Â²Ã Â¸Å¡Ã Â¸Â£Ã Â¸Â·Ã Â¹Ë†Ã Â¸â„¢
		local TweenService = game:GetService("TweenService")
		local tweenInfo = TweenInfo.new(0.15, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)
		local tween = TweenService:Create(gui, tweenInfo, {Position = newPosition})
		tween:Play()
	end
	
	gui.InputBegan:Connect(function(input)
		if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
			dragging = true
			dragStart = input.Position
			startPos = gui.Position
	
			input.Changed:Connect(function()
				if input.UserInputState == Enum.UserInputState.End then
					dragging = false
				end
			end)
		end
	end)
	
	gui.InputChanged:Connect(function(input)
		if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then
			dragInput = input
		end
	end)
	
	UserInputService.InputChanged:Connect(function(input)
		if dragging and input == dragInput then
			update(input)
		end
	end)
	
end
coroutine.wrap(WWJM_fake_script)()

end

local function clamp(value, min, max)
	return math.max(min, math.min(max, value))
end
local self = Nurysium_Util.getBall()
	wait(0.1)
	local Visualize = Instance.new("Part",workspace)
	local Visualize1 = Instance.new("Part",workspace)
	wait(0.5)
	Visualize.Color = Color3.new(0, 1, 0)
	Visualize.Material = Enum.Material.ForceField
	Visualize.Transparency = 0.5
	Visualize.Anchored = true
	Visualize.CanCollide = false
	Visualize.CastShadow = false
	Visualize.Shape = Enum.PartType.Ball
	Visualize.Size = Vector3.new(30,30,30)
	Visualize1.Color = Color3.new(1, 0, 0)
	Visualize1.Material = Enum.Material.ForceField
	Visualize1.Transparency = 0.5
	Visualize1.Anchored = true
	Visualize1.CanCollide = false
	Visualize1.CastShadow = false
	Visualize1.Shape = Enum.PartType.Ball
	Visualize1.Size = Vector3.new(aura_table.spam_Range, aura_table.spam_Range, aura_table.spam_Range)

	local Highlight1 = Instance.new("Highlight")
	Highlight1.Parent = Visualize1
	Highlight1.Enabled = true
	Highlight1.FillTransparency = 0
	Highlight1.OutlineColor = Color3.new(1, 1, 1)
	local Highlight = Instance.new("Highlight")
	Highlight.Parent = Visualize
	Highlight.Enabled = true
	Highlight.FillTransparency = 0
	Highlight.OutlineColor = Color3.new(1, 1, 1)
	
task.spawn(function()
	visualizervar = RunService.RenderStepped:Connect(function()
		if visualize_Enabled then
			Visualize.Transparency = 0
			Visualize.Material = Enum.Material.ForceField
			Visualize.Size = Vector3.new(aura_table.parry_Range, aura_table.parry_Range, aura_table.parry_Range)
			Visualize.CFrame = CFrame.new(local_player.Character.PrimaryPart.Position)
			Visualize1.Transparency = 0
			Visualize1.Material = Enum.Material.ForceField
			Visualize1.Size = Vector3.new(aura_table.spam_Range, aura_table.spam_Range, aura_table.spam_Range)
			Visualize1.CFrame = CFrame.new(local_player.Character.PrimaryPart.Position)
		else
			Visualize.Material = Enum.Material.ForceField
			Visualize.Transparency = 1
			Visualize1.Material = Enum.Material.ForceField
			Visualize1.Transparency = 1
		end	
	end)
end)

function getClosestEntityToMouse()
	local closest = nil
	local shortestDistance = math.huge
	local mouse = game.Players.LocalPlayer:GetMouse()

	-- Ensure workspace.Alive exists
	if not workspace:FindFirstChild("Alive") then
		return nil
	end

	-- Loop through all entities
	for _, entity in pairs(workspace.Alive:GetChildren()) do
		if entity:IsA("Model") then
			local humanoidRootPart = entity:FindFirstChild("HumanoidRootPart")
			if humanoidRootPart then
				-- Convert world position to screen position
				local screenPoint = camera:WorldToViewportPoint(humanoidRootPart.Position)
				local distanceToMouse = (Vector2.new(screenPoint.X, screenPoint.Y) - Vector2.new(mouse.X, mouse.Y)).Magnitude

				-- Check if this is the closest entity so far
				if distanceToMouse < shortestDistance then
					closest = entity
					shortestDistance = distanceToMouse
				end
			else
				
			end
		else
			
		end
	end

	-- If no closest entity is found, warn the user
	if not closest then
		
	else
		
	end

	return closest
end

task.defer(function()
    local runService = game:GetService("RunService")
    local Players = game:GetService("Players")

    local function avoidWalls(startPos, targetPos)
        local direction = (targetPos - startPos).Unit
        local ray = Ray.new(startPos, direction * 10)
        local hit, hitPosition = workspace:FindPartOnRay(ray, local_player.Character)

        if hit then
            -- Wall detected, adjust path
            local adjustedDir = (targetPos - hitPosition).Unit + Vector3.new(0, 0, 0.5) -- Simple adjustment
            return startPos + adjustedDir * 10
        end
return targetPos
    end

    aivar = runService.Heartbeat:Connect(function()
        if not ai_Enabled or not workspace.Alive:FindFirstChild(local_player.Name) then
            return
        end

        local self = Nurysium_Util.getBall()
        if not self or not closest_Entity then
            return
        end

        local hrp = closest_Entity:FindFirstChild('HumanoidRootPart')
        if not hrp then
            walk_to(local_player.Character.HumanoidRootPart.Position + Vector3.new(math.sin(tick()) * math.random(35, 50), 0, math.cos(tick()) * math.random(35, 50)))
            return
        end

        local tickNow = tick()
        local tickMod = tickNow % 4
        local ball_Position = self.Position
        local ball_Distance = local_player:DistanceFromCharacter(ball_Position)
        local player_Position = local_player.Character.PrimaryPart.Position
        local target_Position = hrp.Position
        local target_Distance = local_player:DistanceFromCharacter(target_Position)
        local target_LookVector = hrp.CFrame.LookVector
        local resolved_Position = Vector3.zero

        local target_Humanoid = closest_Entity:FindFirstChildOfClass("Humanoid")
        if target_Humanoid and target_Humanoid:GetState() == Enum.HumanoidStateType.Jumping and local_player.Character.Humanoid.FloorMaterial ~= Enum.Material.Air then
            local_player.Character.Humanoid:ChangeState(Enum.HumanoidStateType.Jumping)
        end

        if (ball_Position - player_Position):Dot(local_player.Character.PrimaryPart.CFrame.LookVector) < -0.2 and tickMod <= 2 then
            return
        end

        -- Maintain distance or get close depending on spamming state
        if aura_table.is_Spamming then
            -- When spamming, move closer to the target
            if tickMod <= 2 then
                resolved_Position = target_Position + (player_Position - target_Position).Unit * 8
            else
                resolved_Position = target_Position - target_LookVector * (math.random(8.5, 13.5) + (ball_Distance / math.random(8, 20)))
            end
        else
            -- Avoid getting too close to other players when not spamming
            for _, player in pairs(Players:GetPlayers()) do
                if player ~= local_player and workspace.Alive:FindFirstChild(player.Name) then
                    local otherPlayerPos = player.Character and player.Character.PrimaryPart.Position
                    if otherPlayerPos and (player_Position - otherPlayerPos).Magnitude < 10 then
                        local avoidanceVector = (player_Position - otherPlayerPos).Unit * 15
                        player_Position = player_Position + avoidanceVector
                    end
                end
            end

            -- Regular pathfinding when not spamming
            if tickMod <= 2 then
                resolved_Position = target_Distance > 10 and target_Position + (player_Position - target_Position).Unit * 25
            else
                resolved_Position = target_Position - target_LookVector * (math.random(8.5, 13.5) + (ball_Distance / math.random(8, 20)))
            end
        end

        if (player_Position - target_Position).Magnitude < 8 then
            resolved_Position = target_Position + (player_Position - target_Position).Unit * 35
        end

        if ball_Distance < 8 then
            resolved_Position = player_Position + (player_Position - ball_Position).Unit * 10
        end

        -- Avoid walls before walking
        resolved_Position = avoidWalls(player_Position, resolved_Position)

        walk_to(resolved_Position + Vector3.new(math.sin(tickNow) * 10, 0, math.cos(tickNow) * 10))
    end)
end)

task.defer(function()
	autowinvar = RunService.Stepped:Connect(function()
		if auto_win and workspace.Alive:FindFirstChild(local_player.Name) then
			local self = Nurysium_Util.getBall()
			if not self then return end
			
			local player = local_player.Character
			local ball_Position = self.Position
			local ball_Distance = (player.HumanoidRootPart.Position - ball_Position).Magnitude
			
			
			local ping = game:GetService("Stats"):FindFirstChild("PerformanceStats"):FindFirstChild("Ping"):GetValue() or 0
			local adjusted_Distance = math.clamp(15 + (ping / 50), 15, 50)

			local angle = tick() * 2
			local offset = Vector3.new(math.cos(angle) * adjusted_Distance, math.sin(angle) * 5, math.sin(angle) * adjusted_Distance)
			local target_Position = ball_Position + offset

			
			player.HumanoidRootPart.CFrame = CFrame.new(target_Position, ball_Position)
		end
	end)
	tphitvar = RunService.Heartbeat:Connect(function()
        	local self = Nurysium_Util.getBall()
	if not self or not tp_hit then return end
	local player = local_player.Character
	local ball_Position = self.Position

	if tp_hit and self:GetAttribute('target') == local_player.Name and workspace.Alive:FindFirstChild(local_player.Name) then

		local safe_Distance = 10
		local direction = (ball_Position - player.HumanoidRootPart.Position).Unit
		local target_Position = ball_Position - direction * safe_Distance

		player.HumanoidRootPart.CFrame = CFrame.new(target_Position)
	end
    end)
end)

local closest_Entity_To_mouse = nil
local Takentime = tick() - aura_table.hit_Time
RunService.Heartbeat:Connect(function()
Takentime = tick() - aura_table.hit_Time
	task.spawn(function()
		closest_Entity_To_mouse = getClosestEntityToMouse()
	end)
end)

task.spawn(function()
    autospamvar = RunService.Heartbeat:Connect(function()
        if not auto_spam or not workspace.Alive:FindFirstChild(local_player.Name) or training_mode then
            aura_table.hit_Count = 0
            aura_table.is_Spamming = false
            aura_table.last_target = nil
            ismyautoparryspamming = false
            aura_table.spam_Range = 0
            return
        end

        if closest_Entity and workspace.Alive:FindFirstChild(closest_Entity.Name) and ((not standalone and aura_table.is_Spamming) or (standalone)) then
            local playerPosition = local_player.Character.PrimaryPart.Position
            local entityPosition = closest_Entity.HumanoidRootPart.Position
            local distanceToEntity = local_player:DistanceFromCharacter(entityPosition)

            if distanceToEntity <= aura_table.spam_Range then
                ismyautoparryspamming = true

                local cf = camera.CFrame
                local direction = (entityPosition - playerPosition).Unit
                local offset = Vector3.new(math.random(-50, 50), math.random(-10, 10), math.random(-50, 50))
                local randomTarget = entityPosition + direction * 50 + offset
                local targetPosition = closest_Entity_To_mouse.HumanoidRootPart.Position
                local fireArgs = {
                    {[closest_Entity_To_mouse.Name] = targetPosition},
                    {targetPosition.X, targetPosition.Y}
                }

                task.defer(function()
                    for count = 1, potanum do
                        if auto_curve then
                            originalParryRemote:FireServer(0, CFrame.new(cf.Position, randomTarget), unpack(fireArgs))
                        else
                            originalParryRemote:FireServer(0, cf, unpack(fireArgs))
                        end
                    end
                end)
            else
                ismyautoparryspamming = false
            end
        else
            ismyautoparryspamming = false
        end
    end)
   

local function linear_predict(a: Vector3, b: Vector3, time_volume: number)
    time_volume = math.clamp(time_volume, 0, 1)
    return a + (b - a) * time_volume
end

autoparryvar = RunService.Heartbeat:Connect(function()
    if not aura_Enabled or not (workspace.Alive:FindFirstChild(local_player.Name) or training_mode) then
        aura_table.hit_Time = tick() * 10
        aura_table.hit_Count = 0
        aura_table.is_ball_Warping = false
        aura_table.is_Spamming = false
        aura_table.canParry = true
        aura_table.last_target = nil
        return
    end

    local ping = Stats.Network.ServerStatsItem["Data Ping"]:GetValue() / 10
    local self

    if training_mode then
        self = getTrainingBall()
    else
        self = Nurysium_Util.getBall()
    end

    if not self then
        aura_table.hit_Time = tick() * 10
        aura_table.hit_Count = 0
        aura_table.is_ball_Warping = false
        aura_table.is_Spamming = false
        aura_table.canParry = true
        aura_table.last_target = nil
        return
    end

    self:GetAttributeChangedSignal('target'):Once(function()
        aura_table.canParry = true
    end)

    if self:GetAttribute('target') ~= local_player.Name or not aura_table.canParry then
        return
    end

    self:GetAttributeChangedSignal('from'):Once(function()
        aura_table.last_target = workspace.Alive:FindFirstChild(self:GetAttribute('from'))
    end)

    get_closest_entity(local_player.Character.PrimaryPart)

    local player_Position = local_player.Character.PrimaryPart.Position
    local ball_Position = self.Position
    local ball_Velocity = self.AssemblyLinearVelocity

    if self:FindFirstChild("zoomies") then
        ball_Velocity = self.zoomies.VectorVelocity
    end

    local ball_Direction = (player_Position - ball_Position).Unit
    local ball_Distance = (player_Position - ball_Position).Magnitude
    local ball_Dot = ball_Direction:Dot(ball_Velocity.Unit)
    local ball_Speed = ball_Velocity.Magnitude

    -- Detección de la bola
    local ball_properties = {}
    ball_properties.position = ball_Position
    ball_properties.velocity = ball_Velocity
    ball_properties.distance = (local_player.Character.PrimaryPart.Position - ball_properties.position).Magnitude
    ball_properties.speed = ball_properties.velocity.Magnitude
    ball_properties.direction = (local_player.Character.PrimaryPart.Position - ball_properties.position).Unit
    ball_properties.dot = ball_properties.direction:Dot(ball_properties.velocity.Unit)
    ball_properties.radians = math.rad(math.asin(ball_properties.dot))

    if ball_properties.dot < -0.2 then
        aura_table.ball_Warping = tick()
    end

    -- Anti-curve mechanism
    if ball_Speed < 25 or ball_Velocity.Y > 10 then
        aura_table.hit_Time = tick() * 10
        aura_table.hit_Count = 0
        aura_table.is_ball_Warping = false
        aura_table.is_Spamming = false
        aura_table.canParry = true
        aura_table.last_target = nil
    end

    local player_Velocity = local_player.Character.HumanoidRootPart.AssemblyLinearVelocity
    local player_isMoving = player_Velocity.Magnitude > 0
    local ball_speed_Limited = math.min(ball_Speed / 1000, 0.1)
    local targetPosition = closest_Entity_To_mouse.HumanoidRootPart.Position
    local target_Distance = local_player:DistanceFromCharacter(targetPosition)
    local closest_target_Distance = local_player:DistanceFromCharacter(closest_Entity.HumanoidRootPart.Position)
    local target_distance_Limited = math.min(target_Distance / 10000, 0.1)
    local target_Direction = (local_player.Character.PrimaryPart.Position - closest_Entity.HumanoidRootPart.Position).Unit
    local target_Velocity = closest_Entity.HumanoidRootPart.AssemblyLinearVelocity
    local target_isMoving = target_Velocity.Magnitude > 0
    local target_Dot = target_isMoving and math.max(target_Direction:Dot(target_Velocity.Unit), 0)

    aura_table.spam_Range = math.clamp(math.max(math.max(ping / 8.5, 15) + ball_Speed / 7.5, 8.4), 25, 1200)
    speedFactor = 3 - (ping / 100)
    speedFactorPingBased = 6.1 - (ping / 100)
    aura_table.parry_Range = math.max(math.max(ping, 3.5) + ball_Speed / speedFactor, speedFactorPingBased)

    aura_table.is_Spamming = aura_table.hit_Count > 1 or (target_Distance <= aura_table.spam_Range and ball_Distance < 18 and ball_Speed > 8) and ball_Velocity.Y > -50 and ball_Dot > 0.15

    task.spawn(function()
        if (tick() - aura_table.ball_Warping) >= 0.15 + target_distance_Limited - ball_speed_Limited or ball_Distance <= 10 then
            aura_table.is_ball_Warping = false
            return
        end

        if aura_table.last_target then
            if (ball_Position - aura_table.last_target.HumanoidRootPart.Position).Magnitude > 35.5 or target_Distance <= 12 then
                aura_table.is_ball_Warping = false
            end
        end

        aura_table.is_ball_Warping = true
    end)

    -- Predecir la posición de la pelota
    local predicted_ball_Position = linear_predict(ball_Position, ball_Position + ball_Velocity * (ping / 100), 0.5)

    if ball_Distance <= aura_table.parry_Range and not aura_table.is_ball_Warping and ball_Speed > 0 and ball_Dot > 0.1 then
        local cf = camera.CFrame
        local target_X = targetPosition.X
        local target_Y = targetPosition.Y

        originalParryRemote:FireServer(
            0,
            CFrame.new(cf.Position, predicted_ball_Position),
            {[closest_Entity_To_mouse.Name] = targetPosition},
            {target_X, target_Y},
            false
        )

        aura_table.hit_Count = aura_table.hit_Count + 1
        task.delay(0.55 + (ping / 100), function()
            aura_table.hit_Count = aura_table.hit_Count - 1
        end)

        aura_table.hit_Time = tick()
        aura_table.canParry = false
    end

    task.spawn(function()
        repeat
            RunService.PreRender:Wait()
        until (tick() - aura_table.hit_Time) >= 1
        aura_table.canParry = true
    end)
end)
end)

-- Define a safe disconnect function to avoid errors
local function safeDisconnect(connection)
    if connection and connection.Disconnect then
        connection:Disconnect()
    end
end

-- Function to manage connections
local function manageConnection(flag, varName, runServiceFunc)
    if flag then
        if not _G[varName] then
            -- Create the RunService connection if the flag is true and connection is not already created
            _G[varName] = RunService[runServiceFunc]:Connect(function()
                -- Your code for what the connection does
            end)
        end
    else
        -- Disconnect and clear the connection if the flag is false
        safeDisconnect(_G[varName])
        _G[varName] = nil
    end
end

-- Main loop running on Heartbeat
RunService.Heartbeat:Connect(function()
    manageConnection(visualize_Enabled, "visualizervar", "Heartbeat")
    manageConnection(auto_spam, "autospamvar", "Heartbeat")
    manageConnection(aura_Enabled, "autoparryvar", "Heartbeat")
    manageConnection(tp_hit, "tphitvar", "Heartbeat")
    manageConnection(auto_win, "autowinvar", "Heartbeat")
    manageConnection(ai_Enabled, "aivar", "RenderStepped")
end)
--[[ to prevent mishaps this linebof code of the ui starts here]]--
				

--// Services
local UserInputService = game:GetService("UserInputService");

--// Library

 				

				
	

												
		
local NoHyper = loadstring(game:HttpGet(("https://raw.githubusercontent.com/3345-c-a-t-s-u-s/NoHyperLib/refs/heads/main/source.dll")))()


NoHyper.set_theme('neverlose') -- [[nohyper , bedol , neverlose, green]]

local Window = NoHyper.new('Star X - Blade ball',"rbxassetid://93079131828771",'The Smootest, Nicest Blade Ball Script') -- My Logo you can replace it
Window:NewSize(UDim2.new(0.1,430,0.1,300))

Window:AddYoutube('https://youtube.com/@starx575')
Window:AddWebsite('https://redhome.carrd.com')
Window:AddDiscord('https://discord.com/invite/EwARkGncq4')

local General = Window:NewTab('Main','earth') -- [[Icon: ads list folder earth locked home positon notify close color]]
local Par = General:NewSection('Parry','','left') -- [left , right]
local Cur = General:NewSection('Curves','','right')
local Far = General:NewSection('Farm','','left') -- [left , right]
local Deb = General:NewSection('Debug','','right')

    	
    	
    	
Par:AddToggle('Auto Parry',false,function(state)
    auto_spam = state
    	aura_Enabled = state
end)
    	
Par:AddDropdown('Method',{Legit,Rage},Rage,function(value)
    print('select ',value)
end)	
    	
Par:AddToggle('Stand Alone mode',false,function(state)
    standalone = state
end)
    	
Par:AddToggle('Manual spam',false,function(state)
            if state then
            ManualSpam()
            else 
            ManualSpam()
            end
end)
    	
Cur:AddToggle('Auto Curve',false,function(state)
    auto_curve = state
end)
    	
Cur:AddToggle('Anti Curve',false,function(state)
    anti_curve_spam_Enabled = state
end)	
    	
Far:AddToggle('Bot play',false,function(state)
    ai_Enabled = state
end)	
    	
Far:AddToggle('Teleport Hit',false,function(state)
    tp_hit = state
end)	
    	
Far:AddToggle('Rage Farm',false,function(state)
    auto_win = state
end)		
    	
Deb:AddToggle('Visualise parry & spam',false,function(state)
    visualize_Enabled = state
end)			

Deb:AddButton('View Console',function()
    game.StarterGui:SetCore("DevConsoleVisible", true)
        wait()
end)	

local TeleportService = game:GetService("TeleportService")

local placeId = 121501154939356

Deb:AddButton('Donate Me!', function()
    local player = game.Players.LocalPlayer
    if player then
        TeleportService:Teleport(placeId, player)
    end
end)
        